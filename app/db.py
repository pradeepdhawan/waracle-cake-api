from functools import lru_cache

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

from app.config.settings import Settings


@lru_cache
def get_settings():
    return Settings()


host = get_settings().postgres_host
port = get_settings().postgres_port
user = get_settings().postgres_user
password = get_settings().postgres_pass
db = get_settings().postgres_db
dbtype = "postgresql"

SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
