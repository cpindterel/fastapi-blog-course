from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("URL: ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#yield turns a regular function into a generator, 
#which produces a sequence of values on demand instead of computing them all at once

#yield a database session, and utilize the session to query the database
def get_db() -> Generator:
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()