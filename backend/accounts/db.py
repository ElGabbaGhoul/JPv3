import motor.motor_asyncio
from bson.objectid import ObjectId

from dotenv import load_dotenv
load_dotenv()
import os

from . import services, models


secret_key=os.getenv('SECRET_KEY')
algorithm=os.getenv('ALGORITHM')
access_token_expires_minutes=os.getenv('ACCESS_TOKEN_EXPIRES_MINUTES')
connection_string = os.environ.get('DB_CONNECTION')

db = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
database = db.UserList
collection = database.user


async def create_user(user):
    document = user
    result = await collection.insert_one(document)
    return document

async def check_db_for_user(username):
    user = await collection.find_one({"username": username})
    return user is not None

async def authenticate_user_by_email(email, plain_password):
    user = await collection.find_one({"username": email})
    if user and await services.verify_password(plain_password, user.get('hashed_password')):
        return models.UserInDB(**user)
    return None

async def fetch_one_user(username):
    user = await collection.find_one({"username": username})
    if user is not None:
        return models.UserInDB(**user)


# Change id to ObjectId(id)
async def update_user(id, user):
    update_result = await collection.update_one({"_id": id}, {"$set": user})
    if update_result.modified_count == 1:
        updated_user = await collection.find_one({"_id": id})
        if updated_user is not None:
            return updated_user
    existing_user = await collection.find_one({"_id": id})
    if existing_user is not None:
        return existing_user


async def remove_user(id):
    await collection.delete_one({"_id": ObjectId(id)})
    return True