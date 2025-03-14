import redis
from ..core.config import settings

def get_redis_client():
    """Get Redis client with SSL support for Redis Cloud"""
    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        ssl=settings.REDIS_SSL,
        decode_responses=True
    )

# Initialize Redis client
redis_client = get_redis_client() 