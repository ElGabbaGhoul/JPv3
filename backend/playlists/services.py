from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from dotenv import load_dotenv
from accounts.models import TokenData, User
# from typing import Optional
import motor.motor_asyncio

load_dotenv()
import os
secret_key=os.getenv('SECRET_KEY')
algorithm=os.getenv('ALGORITHM')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
connection_string = os.environ.get('DB_CONNECTION')


db = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
database = db.UserList
collection = database.user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            print('username is none')
            raise credential_exception
        token_data=TokenData(username=username)


    except JWTError:
      print('JWTError')
      raise credential_exception

    user = await get_user(username=token_data.username)
    print('UNGA BUNGA', type(user))
    if user is None:
        print('user is None')
        raise credential_exception
    
    return user

async def get_user(username:str):
    user = await collection.find_one({"username": username})
    if user:
        return User(**user)
    
    else:
        return None