import os
import motor.motor_asyncio  # MongoDB Driver

from dotenv import load_dotenv
load_dotenv()
connection_string = os.environ.get('DB_CONNECTION')

client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
database = client.PlaylistList
collection = database.playlist

async def create_playlist(playlist):
    document = playlist
    result = await collection.insert_one(document)
    return document