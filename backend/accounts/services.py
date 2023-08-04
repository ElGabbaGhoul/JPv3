from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt, JWTError
from . import models, db

from dotenv import load_dotenv
load_dotenv()
import os
secret_key=os.getenv('SECRET_KEY')
algorithm=os.getenv('ALGORITHM')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password):
    return pwd_context.hash(password)

async def verify_password(plain_password, hashed_password):
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