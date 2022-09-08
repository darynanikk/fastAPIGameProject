from typing import List

from pydantic import BaseModel, EmailStr


class GameBase(BaseModel):
    name: str


class Game(GameBase):
    id: int
    player_id: int


class GameCreate(GameBase):
    pass


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    name: str
    age: int
    email: EmailStr

    class Config:
        orm_mode = True


class GameInfo(BaseModel):
    user: User
    games: List[str]
    completed: bool = False
    turn: int = 200


class CreateUser(UserBase):
    name: str
    age: int
    email: EmailStr
    game: str


class UserOut(UserBase):
    games: List[GameBase]


class GameOut(GameBase):
    users: List[User]
