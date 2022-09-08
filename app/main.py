from app import services

from sqlalchemy.orm import Session
from starlette import status
from fastapi import Depends, FastAPI, HTTPException
from app.database import SessionLocal, engine
from app.db.schemas import CreateUser, GameInfo

services.models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/connect/", status_code=status.HTTP_201_CREATED)
def connect_to_game(user: CreateUser, db: Session = Depends(get_db)):
    try:
        user_email = user.email
        game = user.game
        player = services.get_user_by_email(db=db, email=user_email)
        if not player:
            player = services.create_user(db=db, user=user)
        services.connect(db=db, game_name=game, player_id=player.id)
        return {"connected"}
    except ValueError as exp:
        return exp


@app.get("/games/", response_model=list)
def get_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = services.get_games(db, skip=skip, limit=limit)
    game_users = []
    for game in games:
        game_users.append({
            'game': game.name,
            'users': game.users
        })
    return game_users


@app.get("/me/{user_id}")
def get_me(user_id: int, db: Session = Depends(get_db)):
    try:
        user, games = services.get_player_games(db=db, player_id=user_id)
        game_info = GameInfo(user=user, games=[game.name for game in games], completed=True)
        return game_info
    except HTTPException as exp:
        return exp
