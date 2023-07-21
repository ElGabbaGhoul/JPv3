from fastapi import APIRouter, Body, Depends, HTTPException
from . import models, db, services
from fastapi.encoders import jsonable_encoder
from accounts.models import User

router = APIRouter()

# response_model=models.Playlist,
# Playlist CRUD
@router.post("/api/playlist", response_description="Create a new playlist", tags=['playlists'])
async def create_new_playlist(playlist: models.Playlist = Body(...), current_user: User = Depends(services.get_current_user)):
    playlist.created_by = str(current_user.id)
    playlist_dict = jsonable_encoder(playlist)
    response = await db.create_playlist(playlist_dict)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")


# @router.get("/api/playlist", response_description="Create a new playlist", tags=['playlists'])
# async def get_users_playlists(current_user: User = Depends(services.get_current_user)):


#     if response:
#         return response
#     raise HTTPException(400, "Something went wrong / Bad Request")