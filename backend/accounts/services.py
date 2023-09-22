from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt, JWTError
from . import models, db

pepper = "a9d0a8w09a8f-a9w-a89afa6wa5sxhvkfgmfgh981?"
joiner = "quwieoasjkdlxzcnvm,00"

from dotenv import load_dotenv
load_dotenv()
import os
secret_key=os.getenv('SECRET_KEY')
algorithm=os.getenv('ALGORITHM')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Salt:
# Random value generated uniquely for each user's pw
# When user creates or updates their pw, random salt is generated and combined w their pw before hashing
# salt is then stored alongside hashedpw in the db
# ensures identical pwds do not result in same hash value. Makes precomputed tables less effective.
# Adds randomness to hashing process, making it computationally infeasible to use brute force/dictionary attacks

# Pepper:
# Random value, different than salt, kept secret & not stored alongside hashedpw in db
# pepper typically added to pw before hashing, like salt, but is constant for all users and apps
# kept secret within app's code/config, is not exposed in db (env?)
# adds extra security. Even if attacker gains access to db and knows hashing algo andd salt, still won't be crackable
# security of pepper relies on secrecy. if pepper is compromised can severely weaken security of pw storage

def get_password_hash(password):
    return pepper + joiner + pwd_context.hash(password)

async def verify_password(plain_password, hashed_password):
    print(hashed_password)
    fully_hashed = hashed_password.split(joiner)
    print(fully_hashed)
    hashed_password = fully_hashed[1]
    return pwd_context.verify(plain_password, hashed_password)

async def create_access_token(data: dict, expires_delta: timedelta or None=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else: 
      expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth_2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials - accounts",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        print('right before the payload comes this string')
        print('TOKEN HERE', token)
        print('KEY HERE', secret_key)
        print('ALGO HERE', algorithm)
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        print("THIS IS THE PAYLOAD", payload)
        username: str = payload.get("sub")
        print("THIS IS THE USERNAME", username)
        if username is None:
            print('error1')
            raise credential_exception
        token_data = models.TokenData(username=username)
    except JWTError:
        print('error2')
        raise credential_exception
    user = await db.fetch_one_user(username=token_data.username)
    if user is None:
        print('error3')
        raise credential_exception
    print(f'user id: {user.id}')
    return user

async def get_current_active_user(
    current_user: models.UserInDB = Depends(get_current_user),
):
    return current_user