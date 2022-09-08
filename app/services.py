from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db import models, schemas
from app.db.schemas import GameCreate


# Get games (get list of all games and users who connected to this games)
# Get me (get info about current user and info about all connected games)
# Connect to game. When user send this request. Need to create one obj like User - Game.


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(email=user.email, name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def connect(db: Session, game_name: str, player_id: str):
    user = db.query(models.User).filter(models.User.id == player_id).first()
    game = db.query(models.Game).filter(models.Game.name == game_name).first()
    if game is None:
        game = create_game(db=db, game=GameCreate(name=game_name, player_id=player_id))
    if user not in game.users:
        game.users.append(user)
        db.add(game)
        db.commit()
    return user


def create_game(db: Session, game: schemas.GameCreate, **fields):
    db_game = models.Game(name=game.name)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_player_games(db: Session, player_id: int):
    user = db.query(models.User).get(player_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    games = user.games
    return user, games


def get_games(db: Session, skip: int = 0, limit: int = 10):
    """get list of all games and users who connected to this games."""
    return db.query(models.Game).offset(skip).limit(limit).all()
