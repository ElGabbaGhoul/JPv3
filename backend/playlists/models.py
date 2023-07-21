from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

# from Backend_Accounts.models import TokenData, UserInDB



class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Song(BaseModel):
    title: str
    artist: str
    duration: int # Duration of song in seconds

class Playlist(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: str
    created_by: str # User ID of creator
    created_on: str
    updated_on: str
    tracks: List[Song]
    duration: int # Total playlist duration in seconds
    is_public: bool
    tags: List[str]
    creator_notes: Optional[str]
    image_url: Optional[str]
    listener_comments: Optional[List[str]]
    collaborators: Optional[List[str]] = []
    is_collaborative: Optional[bool] = False


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                    'name': '',
                    'description': '',
                    'created_by': '',
                    'created_on': '',
                    'updated_on': '',
                    'tracks': [
                        {"title": "", "artist": "", "duration": 000},
                        {"title": "", "artist": "", "duration": 000}
                    ],
                    'duration': 43000,
                    'is_public': True,
                    'tags': ['cool', 'epic', 'genre'],
                    'creator_notes': 'I made this',
                    'image_url': 'https://media.giphy.com/media/WWvteK57VNvxu/giphy.gif',
                    'listener_comments': ['wow what a great playlist', 'this is awesome', 'who made this?']
            }
        }


class UpdatePlaylistModel(BaseModel):
    name: Optional[str] 
    description: Optional[str] 
    created_on: Optional[str]
    updated_on: Optional[str] 
    created_by: Optional[str] 
    owner_id: Optional[str] 
    tracks: Optional[list]
    duration: Optional[int] 
    is_public: Optional[bool] 
    tags: Optional[list]
    creator_notes: Optional[str] 
    image_url: Optional[str]
    listener_comments: Optional[list] 
    collaborators: Optional[List[str]] = []
    is_collaborative: Optional[bool]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                    'name': '',
                    'description': '',
                    'created_by': '',
                    'created_on': '',
                    'updated_on': '',
                    'tracks': [
                        {"title": "", "artist": "", "duration": 000},
                        {"title": "", "artist": "", "duration": 000}
                    ],
                    'duration': 43000,
                    'is_public': True,
                    'tags': ['cool', 'epic', 'genre'],
                    'creator_notes': 'I made this',
                    'image_url': 'https://media.giphy.com/media/WWvteK57VNvxu/giphy.gif',
                    'listener_comments': ['wow what a great playlist', 'this is awesome', 'who made this?']
            }
        }