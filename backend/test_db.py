from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config
import asyncio

async def test_connection():
    try:
        # Get MongoDB URL from environment
        mongodb_url = config('MONGODB_URL')
        
        # Create client
        client = AsyncIOMotorClient(mongodb_url)
        
        # Test connection
        await client.admin.command('ping')
        print("✅ Successfully connected to MongoDB Atlas!")
        
        # List databases
        database_names = await client.list_database_names()
        print("\nAvailable databases:")
        for db in database_names:
            print(f"- {db}")
            
    except Exception as e:
        print("❌ Connection failed!")
        print(f"Error: {str(e)}")
    finally:
        # Close connection
        client.close()

if __name__ == "__main__":
    asyncio.run(test_connection()) 