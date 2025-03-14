from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from ....models.user import User
from ....models.resume import Resume, ResumeCreate, ResumeUpdate
from ....services.resume_service import (
    upload_resume,
    create_resume,
    get_resume,
    get_user_resume,
    update_resume,
    delete_resume,
    analyze_resume_for_role
)
from ....core.deps import get_current_user

router = APIRouter()

@router.post("/upload")
async def upload_resume_file(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    """Upload a resume file"""
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed"
        )
    
    file_content = await file.read()
    file_url = await upload_resume(str(current_user.id), file_content, file.filename)
    
    return {"file_url": file_url}

@router.post("", response_model=Resume)
async def create_new_resume(
    resume_data: ResumeCreate,
    current_user: User = Depends(get_current_user)
):
    """Create a new resume entry"""
    return await create_resume(str(current_user.id), resume_data)

@router.get("/me", response_model=Resume)
async def get_my_resume(current_user: User = Depends(get_current_user)):
    """Get current user's active resume"""
    resume = await get_user_resume(str(current_user.id))
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active resume found"
        )
    return resume

@router.get("/{resume_id}", response_model=Resume)
async def get_resume_by_id(
    resume_id: str,
    current_user: User = Depends(get_current_user)
):
    """Get a specific resume by ID"""
    resume = await get_resume(resume_id)
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    if str(resume.user_id) != str(current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this resume"
        )
    
    return resume

@router.put("/{resume_id}", response_model=Resume)
async def update_resume_details(
    resume_id: str,
    resume_update: ResumeUpdate,
    current_user: User = Depends(get_current_user)
):
    """Update a resume"""
    resume = await get_resume(resume_id)
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    if str(resume.user_id) != str(current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this resume"
        )
    
    return await update_resume(resume_id, resume_update)

@router.delete("/{resume_id}")
async def delete_resume_by_id(
    resume_id: str,
    current_user: User = Depends(get_current_user)
):
    """Delete a resume"""
    resume = await get_resume(resume_id)
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    if str(resume.user_id) != str(current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this resume"
        )
    
    success = await delete_resume(resume_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete resume"
        )
    return {"message": "Resume deleted successfully"}

@router.post("/{resume_id}/analyze/{role_id}")
async def analyze_resume_role_match(
    resume_id: str,
    role_id: str,
    current_user: User = Depends(get_current_user)
):
    """Analyze resume against a specific role"""
    resume = await get_resume(resume_id)
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    if str(resume.user_id) != str(current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this resume"
        )
    
    return await analyze_resume_for_role(resume_id, role_id) 