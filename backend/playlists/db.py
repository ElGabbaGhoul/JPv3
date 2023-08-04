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

async def fetch_playlists_by_user_id(user_id):
    document = await collection.find({"created_by": str(user_id)}).to_list(length=None)
    print(f'fetching playlists created by user id of {user_id}...')
    return document

async def fetch_playlist_by_id(id):
    document = await collection.find_one({"_id": id})
    print(f'fetching playlist with id of {id}...')
    return document