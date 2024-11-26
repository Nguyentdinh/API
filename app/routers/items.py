# app/routers/items.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_items():
    return {"message": "List of items"}
