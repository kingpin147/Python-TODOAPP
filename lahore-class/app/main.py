from fastapi import FastAPI
from sqlmodel import SQLModel
from app import settings
from contextlib import contextmanager
from sqlalchemy import create_engine


app=FastAPI(title="Lahore Class", version="1.0.0")


class TODO(SQLModel, table=True):
 id: int | None = None
 content: str
 
 connection_string = str(settings.DATABASE_URL).replace
 "postgressql", "postgresql+psycopg2"



engine = create_engine(settings.DATABASE_URL)
(connection_string)





@app.get("/teachers")
def read_teachers():
 return {"teacher": "Sir Qasim"}  
        
@app.get("/")
def read_root():
 return {"teacher": "Sir Qasim"}  
