import os

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()
# change to True when running docker-compose up --build
DEBUG = False

DATABASE_URL = 'DATABASE_URL'

if DEBUG:
    DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_LOCALHOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


class Settings(BaseSettings):
    db_url: str = Field(env=DATABASE_URL, default=DATABASE_URL)


settings = Settings()
