from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from sql_app.items.schemas import Item
from sql_app.items.crud import get_items
from sql_app.auth import get_db

items_router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@items_router.get("/", response_model=List[Item])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items
