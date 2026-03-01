from fastapi import FastAPI
from app.services import get_top_expensive, get_free_games

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Steam Data API Running"}

@app.get("/top-expensive")
def top_expensive():
    return get_top_expensive()

@app.get("/free-games")
def free_games():
    return get_free_games()