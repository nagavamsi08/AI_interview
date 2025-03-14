from typing import List, Optional
from fastapi import HTTPException
from ..db.mongodb import find_one, find_many, insert_one, update_one
from ..models.role import Role, RoleCreate, RoleUpdate, Skill

async def create_role(role_data: RoleCreate) -> Role:
    # Create role
    role = Role(
        **role_data.dict(),
        is_active=True
    )
    
    role_id = await insert_one("roles", role.dict(by_alias=True))
    role.id = role_id
    
    return role

async def get_role(role_id: str) -> Optional[Role]:
    role_dict = await find_one("roles", {"_id": role_id})
    if role_dict:
        return Role(**role_dict)
    return None

async def get_roles(
    category: Optional[str] = None,
    specialization: Optional[str] = None,
    experience_level: Optional[str] = None,
    is_active: bool = True
) -> List[Role]:
    # Build query
    query = {"is_active": is_active}
    if category:
        query["category"] = category
    if specialization:
        query["specialization"] = specialization
    if experience_level:
        query["experience_level"] = experience_level
    
    roles = await find_many("roles", query)
    return [Role(**r) for r in roles]

async def update_role(role_id: str, role_update: RoleUpdate) -> Role:
    # Get existing role
    role = await get_role(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    # Update role
    update_data = role_update.dict(exclude_unset=True)
    updated = await update_one(
        "roles",
        {"_id": role_id},
        update_data
    )
    
    if not updated:
        raise HTTPException(
            status_code=500,
            detail="Failed to update role"
        )
    
    return await get_role(role_id)

async def deactivate_role(role_id: str) -> bool:
    updated = await update_one(
        "roles",
        {"_id": role_id},
        {"is_active": False}
    )
    return bool(updated)

async def get_role_skills(role_id: str) -> dict:
    role = await get_role(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    return {
        "required_skills": [s.dict() for s in role.required_skills],
        "preferred_skills": [s.dict() for s in role.preferred_skills]
    }

async def add_skill_to_role(
    role_id: str,
    skill: Skill,
    importance: str = "required"
) -> Role:
    role = await get_role(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    # Add skill to appropriate list
    if importance == "required":
        role.required_skills.append(skill)
    else:
        role.preferred_skills.append(skill)
    
    # Update role
    updated = await update_one(
        "roles",
        {"_id": role_id},
        {
            "required_skills" if importance == "required" else "preferred_skills":
            [s.dict() for s in (role.required_skills if importance == "required" else role.preferred_skills)]
        }
    )
    
    if not updated:
        raise HTTPException(
            status_code=500,
            detail="Failed to update role skills"
        )
    
    return role

async def remove_skill_from_role(
    role_id: str,
    skill_name: str,
    importance: str = "required"
) -> Role:
    role = await get_role(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    # Remove skill from appropriate list
    if importance == "required":
        role.required_skills = [s for s in role.required_skills if s.name != skill_name]
    else:
        role.preferred_skills = [s for s in role.preferred_skills if s.name != skill_name]
    
    # Update role
    updated = await update_one(
        "roles",
        {"_id": role_id},
        {
            "required_skills" if importance == "required" else "preferred_skills":
            [s.dict() for s in (role.required_skills if importance == "required" else role.preferred_skills)]
        }
    )
    
    if not updated:
        raise HTTPException(
            status_code=500,
            detail="Failed to update role skills"
        )
    
    return role

async def get_role_statistics() -> dict:
    roles = await find_many("roles", {"is_active": True})
    
    categories = {}
    experience_levels = {
        "fresher": 0,
        "mid-level": 0,
        "senior": 0
    }
    total_roles = len(roles)
    
    for role in roles:
        # Count by category
        category = role["category"]
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1
        
        # Count by experience level
        experience_levels[role["experience_level"]] += 1
    
    return {
        "total_roles": total_roles,
        "categories": categories,
        "experience_levels": experience_levels
    } 