from typing import List
from pydantic import BaseModel

from src.items.schemas import Item
from src.company.schemas import CompanyBase


class UserBase(BaseModel):
    company: CompanyBase
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
