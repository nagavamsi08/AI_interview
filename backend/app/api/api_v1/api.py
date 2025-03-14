from fastapi import APIRouter
from .endpoints import users, interviews, resumes, roles

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(interviews.router, prefix="/interviews", tags=["interviews"])
api_router.include_router(resumes.router, prefix="/resumes", tags=["resumes"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"]) 