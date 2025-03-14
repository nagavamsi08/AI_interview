from fastapi import Request
from fastapi.responses import JSONResponse
from .exceptions import AIInterviewException
from typing import Union, Dict, Any
import traceback
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def error_handler(request: Request, exc: Exception) -> JSONResponse:
    """Global error handler"""
    
    if isinstance(exc, AIInterviewException):
        # Handle our custom exceptions
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )
    
    # Log unexpected errors
    logger.error(f"Unexpected error occurred: {str(exc)}")
    logger.error(traceback.format_exc())
    
    # Return generic error for unexpected exceptions
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected error occurred. Please try again later."
        }
    )

class ErrorLoggingMiddleware:
    """Middleware for logging requests and errors"""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, request: Request, call_next):
        try:
            # Log request
            logger.info(f"Request: {request.method} {request.url}")
            
            # Process request
            response = await call_next(request)
            
            # Log response status
            logger.info(f"Response: {response.status_code}")
            
            return response
            
        except Exception as exc:
            # Handle error
            return await error_handler(request, exc)

class RateLimitMiddleware:
    """Middleware for rate limiting"""
    
    def __init__(self, app):
        self.app = app
        # Initialize rate limiting (you can use Redis for distributed setup)
        self.requests = {}
    
    async def __call__(self, request: Request, call_next):
        # Implement rate limiting logic here
        # This is a simple example; in production, use Redis or similar
        client_ip = request.client.host
        
        # Check rate limit
        if self._is_rate_limited(client_ip):
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Too many requests. Please try again later."
                }
            )
        
        return await call_next(request)
    
    def _is_rate_limited(self, client_ip: str) -> bool:
        # Implement your rate limiting logic here
        return False  # Placeholder

class SecurityHeadersMiddleware:
    """Middleware for adding security headers"""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, request: Request, call_next):
        response = await call_next(request)
        
        # Add security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        
        return response 