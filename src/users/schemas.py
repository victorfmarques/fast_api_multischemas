from typing import List
from pydantic import BaseModel

from src.items.schemas import Item
from src.company.schemas import CompanyBase


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
