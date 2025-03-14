from fastapi import HTTPException, status

class AIInterviewException(HTTPException):
    """Base exception for AI Interview Platform"""
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

class NotFoundError(AIInterviewException):
    """Resource not found"""
    def __init__(self, resource: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} not found"
        )

class UnauthorizedError(AIInterviewException):
    """Unauthorized access"""
    def __init__(self, message: str = "Not authorized to perform this action"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=message
        )

class ValidationError(AIInterviewException):
    """Validation error"""
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )

class FileUploadError(AIInterviewException):
    """File upload error"""
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File upload failed: {message}"
        )

class DatabaseError(AIInterviewException):
    """Database operation error"""
    def __init__(self, operation: str):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database operation failed: {operation}"
        )

class ExternalServiceError(AIInterviewException):
    """External service error"""
    def __init__(self, service: str, message: str):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"{service} service error: {message}"
        ) 