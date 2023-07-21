from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt

from dotenv import load_dotenv
load_dotenv()
import os
secret_key=os.getenv('SECRET_KEY')
algorithm=os.getenv('ALGORITHM')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



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