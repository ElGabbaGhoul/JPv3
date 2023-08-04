from fastapi import APIRouter, Body, Depends, HTTPException, Path
from . import models, db, services
from fastapi.encoders import jsonable_encoder
from accounts.models import User

router = APIRouter()

# response_model=models.Playlist,
# Playlist CRUD
@router.post("/api/playlist", response_description="Create a new playlist", tags=['playlists api'])
async def create_new_playlist(playlist: models.Playlist = Body(...), current_user: User = Depends(services.get_current_user)):
    playlist.created_by = str(current_user.id)
    playlist_dict = jsonable_encoder(playlist)
    response = await db.create_playlist(playlist_dict)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")


@router.get("/api/playlist/{user_id}", response_description="Get playlists by user", tags=['playlists api'])
async def get_users_playlists(
    user_id: str = Path(..., title="User ID", description="The ID of the user to retrieve playlists for."),
    current_user: User = Depends(services.get_current_user)):
    if user_id != str(current_user.id):
      raise HTTPException(403, "You are not allowed to access other users' playlists!")

    playlists = await db.fetch_playlists_by_user_id(current_user.id)
    if playlists:
      print("here's what I found")
      return playlists
    return []

@router.get("/api/playlist/id/{id}", response_description="Get playlists by playlist id", tags=['playlists api'])
async def get_playlist_by_id(id):
    playlist = await db.fetch_playlist_by_id(id)
    if playlist:
      print("here's what I found")
      return playlist
