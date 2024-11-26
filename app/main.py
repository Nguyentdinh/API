# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.database import get_db

app = FastAPI()

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users
