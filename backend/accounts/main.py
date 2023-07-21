# API Endpoints for accounts. Incoming requests, retrieving data from database/models, returns responses
# Declares router, import dependencies from crud.py and models.py
# contains route handlers

from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()
import os

access_token_expires_minutes=int(os.getenv('ACCESS_TOKEN_EXPIRES_MINUTES'))


from . import models, db, services

router = APIRouter()

# Token
@router.post("/token", response_model=models.Token, tags=['auth'])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    plain_password = form_data.password
    user = await db.authenticate_user_by_email(email, plain_password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=access_token_expires_minutes)
    print(f'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',user)
    access_token = await services.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# Account CRUD
@router.post("/api/user", response_description="Create new user", response_model=models.User, tags=['users'])
async def create_new_user(user: models.UserInDB = Body(...)):
    # Check if email already exists in database
    existing_user = await db.check_db_for_user(user.username)
    if existing_user:
        raise HTTPException(status_code=409, detail="User with username already exists")

    # Hash password
    user.hashed_password = services.get_password_hash(user.hashed_password)

    # Create user
    user_dict = jsonable_encoder(user)
    response = await db.create_user(user_dict)
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong / Bad Request")

@router.get("/api/user/{username}", response_description="Get a single user", response_model=models.User, tags=['users'])
async def get_user_by_username(username: str):
    response = await db.fetch_one_user(username)
    if response:
        return response
    raise HTTPException(404, f"User with username {username} not found")

# Does not work after changing {id} to {username}
@router.put("/api/user/{id}", response_description="Update a user", response_model=models.User, tags=['users'])
async def put_user(id: str, user: models.UpdateUserModel = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}
    if len(user) >= 1:
        response = await db.update_user(id, user)
    if response:
        return response
    raise HTTPException(404, f"User {id} not found.")

@router.delete("/api/user/{id}", response_description="Delete a user", tags=['users'])
async def delete_user(id: str):
    response = await db.remove_user(id)
    if response:
        return "Successfully deleted user item"
    raise HTTPException(404, f"User with ID of {id} not found.")