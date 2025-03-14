from typing import Optional, Dict
import boto3
from fastapi import HTTPException
from ..core.config import settings
from ..db.mongodb import find_one, insert_one, update_one
from ..models.resume import Resume, ResumeCreate, ResumeUpdate, ParsedResumeData
from ..services.ai_service import analyze_resume

# Initialize S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION
)

async def upload_resume(user_id: str, file_content: bytes, filename: str) -> str:
    """Upload resume to S3 and return the file URL"""
    try:
        # Generate S3 key
        s3_key = f"resumes/{user_id}/{filename}"
        
        # Upload to S3
        s3_client.put_object(
            Bucket=settings.S3_BUCKET,
            Key=s3_key,
            Body=file_content,
            ContentType='application/pdf'
        )
        
        # Generate URL
        url = f"https://{settings.S3_BUCKET}.s3.{settings.AWS_REGION}.amazonaws.com/{s3_key}"
        return url
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to upload resume: {str(e)}"
        )

async def create_resume(user_id: str, resume_data: ResumeCreate) -> Resume:
    # Check if user already has an active resume
    existing_resume = await find_one(
        "resumes",
        {"user_id": user_id, "status": "active"}
    )
    
    if existing_resume:
        # Archive existing resume
        await update_one(
            "resumes",
            {"_id": existing_resume["_id"]},
            {"status": "archived"}
        )
    
    # Parse resume
    parsed_data = await analyze_resume(resume_data.file_url)
    
    # Create new resume
    resume = Resume(
        user_id=user_id,
        original_file=resume_data.file_url,
        parsed_data=ParsedResumeData(**parsed_data["parsed_data"]),
        confidence_score=parsed_data["confidence_score"],
        skill_matches=parsed_data["skill_matches"]
    )
    
    resume_id = await insert_one("resumes", resume.dict(by_alias=True))
    resume.id = resume_id
    
    return resume

async def get_resume(resume_id: str) -> Optional[Resume]:
    resume_dict = await find_one("resumes", {"_id": resume_id})
    if resume_dict:
        return Resume(**resume_dict)
    return None

async def get_user_resume(user_id: str) -> Optional[Resume]:
    resume_dict = await find_one(
        "resumes",
        {"user_id": user_id, "status": "active"}
    )
    if resume_dict:
        return Resume(**resume_dict)
    return None

async def update_resume(resume_id: str, resume_update: ResumeUpdate) -> Resume:
    # Get existing resume
    resume = await get_resume(resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    # Update resume
    update_data = resume_update.dict(exclude_unset=True)
    updated = await update_one(
        "resumes",
        {"_id": resume_id},
        update_data
    )
    
    if not updated:
        raise HTTPException(
            status_code=500,
            detail="Failed to update resume"
        )
    
    return await get_resume(resume_id)

async def delete_resume(resume_id: str) -> bool:
    # Soft delete by updating status
    updated = await update_one(
        "resumes",
        {"_id": resume_id},
        {"status": "deleted"}
    )
    return bool(updated)

async def analyze_resume_for_role(resume_id: str, role_id: str) -> Dict:
    # Get resume and role
    resume = await get_resume(resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    role_dict = await find_one("roles", {"_id": role_id})
    if not role_dict:
        raise HTTPException(status_code=404, detail="Role not found")
    
    # Analyze skill match
    required_skills = {s["name"]: s["level"] for s in role_dict["required_skills"]}
    preferred_skills = {s["name"]: s["level"] for s in role_dict["preferred_skills"]}
    candidate_skills = set(resume.parsed_data.skills)
    
    # Calculate matches
    required_matches = {
        skill: level
        for skill, level in required_skills.items()
        if skill in candidate_skills
    }
    
    preferred_matches = {
        skill: level
        for skill, level in preferred_skills.items()
        if skill in candidate_skills
    }
    
    # Calculate scores
    required_score = len(required_matches) / len(required_skills) if required_skills else 1.0
    preferred_score = len(preferred_matches) / len(preferred_skills) if preferred_skills else 1.0
    
    overall_score = required_score * 0.7 + preferred_score * 0.3
    
    return {
        "overall_match_score": overall_score,
        "required_skills_score": required_score,
        "preferred_skills_score": preferred_score,
        "missing_required_skills": [
            skill for skill in required_skills
            if skill not in candidate_skills
        ],
        "missing_preferred_skills": [
            skill for skill in preferred_skills
            if skill not in candidate_skills
        ],
        "skill_matches": {
            "required": required_matches,
            "preferred": preferred_matches
        }
    } 