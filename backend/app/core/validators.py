from typing import List
from .exceptions import ValidationError
import re

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError("Invalid email format")
    return True

def validate_password(password: str) -> bool:
    """
    Validate password strength:
    - At least 8 characters
    - Contains uppercase and lowercase letters
    - Contains numbers
    - Contains special characters
    """
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")
    
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one number")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError("Password must contain at least one special character")
    
    return True

def validate_file_size(size: int, max_size_mb: int = 10) -> bool:
    """Validate file size"""
    max_size_bytes = max_size_mb * 1024 * 1024
    if size > max_size_bytes:
        raise ValidationError(f"File size exceeds maximum limit of {max_size_mb}MB")
    return True

def validate_file_type(filename: str, allowed_extensions: List[str]) -> bool:
    """Validate file type"""
    ext = filename.lower().split('.')[-1]
    if ext not in allowed_extensions:
        raise ValidationError(f"File type not allowed. Allowed types: {', '.join(allowed_extensions)}")
    return True

def validate_interview_status(status: str) -> bool:
    """Validate interview status"""
    valid_statuses = ["scheduled", "in_progress", "completed", "paused", "abandoned"]
    if status not in valid_statuses:
        raise ValidationError(f"Invalid interview status. Valid statuses: {', '.join(valid_statuses)}")
    return True

def validate_role_category(category: str) -> bool:
    """Validate role category"""
    valid_categories = ["Data Science", "Web Development"]
    if category not in valid_categories:
        raise ValidationError(f"Invalid role category. Valid categories: {', '.join(valid_categories)}")
    return True

def validate_experience_level(level: str) -> bool:
    """Validate experience level"""
    valid_levels = ["fresher", "mid-level", "senior"]
    if level not in valid_levels:
        raise ValidationError(f"Invalid experience level. Valid levels: {', '.join(valid_levels)}")
    return True

def validate_skill_level(level: str) -> bool:
    """Validate skill level"""
    valid_levels = ["beginner", "intermediate", "advanced"]
    if level not in valid_levels:
        raise ValidationError(f"Invalid skill level. Valid levels: {', '.join(valid_levels)}")
    return True

def validate_skill_importance(importance: str) -> bool:
    """Validate skill importance"""
    valid_importance = ["required", "preferred"]
    if importance not in valid_importance:
        raise ValidationError(f"Invalid skill importance. Valid values: {', '.join(valid_importance)}")
    return True

def validate_language(language: str) -> bool:
    """Validate language code"""
    valid_languages = ["en", "fr", "ar"]  # Add more as needed
    if language not in valid_languages:
        raise ValidationError(f"Invalid language code. Valid codes: {', '.join(valid_languages)}")
    return True 