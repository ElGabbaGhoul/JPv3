# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from accounts import main as accounts_api
from playlists import main as playlists_api

app = FastAPI()

app.include_router(accounts_api.router)
app.include_router(playlists_api.router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)