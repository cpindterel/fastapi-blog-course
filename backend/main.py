from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base

def create_tables():
    Base.metadata.create_all(bind=engine) 

def start_application(): #entry point, responsable for creating tables and returning to app
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app

app = start_application()


app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def hello():
    return {"msg": "Hello FastAPI"}