from typing import Generator

from pymongo import MongoClient
from pymongo.database import Database

from app.core.config import settings

client = MongoClient(settings.MONGODB_URL)

def get_database() -> Database:
    return client[settings.MONGODB_DB_NAME]

async def connect_to_mongo():
    # Create indexes
    await create_indexes()

async def close_mongo_connection():
    if client:
        client.close()

async def create_indexes():
    # Users collection indexes
    await get_database().users.create_index("email", unique=True)
    
    # Resumes collection indexes
    await get_database().resumes.create_index("user_id")
    await get_database().resumes.create_index("status")
    
    # Interviews collection indexes
    await get_database().interviews.create_index("user_id")
    await get_database().interviews.create_index("role_id")
    await get_database().interviews.create_index("status")
    await get_database().interviews.create_index([("start_time", -1)])
    
    # Questions collection indexes
    await get_database().questions.create_index("interview_id")
    await get_database().questions.create_index([("type", 1), ("difficulty", 1)])
    
    # Answers collection indexes
    await get_database().answers.create_index("question_id")
    
    # Roles collection indexes
    await get_database().roles.create_index([("category", 1), ("specialization", 1)])
    await get_database().roles.create_index("experience_level")

# Helper functions for CRUD operations
async def insert_one(collection: str, document: dict):
    result = await get_database()[collection].insert_one(document)
    return result.inserted_id

async def find_one(collection: str, query: dict):
    return await get_database()[collection].find_one(query)

async def find_many(collection: str, query: dict, limit: int = 0):
    cursor = get_database()[collection].find(query)
    if limit > 0:
        cursor = cursor.limit(limit)
    return await cursor.to_list(None)

async def update_one(collection: str, query: dict, update: dict):
    result = await get_database()[collection].update_one(query, {"$set": update})
    return result.modified_count

async def delete_one(collection: str, query: dict):
    result = await get_database()[collection].delete_one(query)
    return result.deleted_count

async def aggregate(collection: str, pipeline: list):
    return await get_database()[collection].aggregate(pipeline).to_list(None) 