from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, validates

from app.database import Base

user_game = Table("user_game", Base.metadata,
                  Column("user_id", ForeignKey("user.id"), primary_key=True),
                  Column("game_id", ForeignKey("game.id"), primary_key=True))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)
    games = relationship("Game",
                         secondary=user_game,
                         back_populates="users")

    @validates('age')
    def validate_age(self, key, value):
        if value <= 0 or value >= 100:
            raise ValueError("Age should be greater than 0 and less than 100")
        return value


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    users = relationship("User",
                         secondary=user_game,
                         back_populates="games")
