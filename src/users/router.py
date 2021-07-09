from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from src.auth import oauth2_scheme, get_schemaless_db

from src.company import crud as company_crud

from src.users.schemas import User, UserCreate
from src.users import crud


users_router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@users_router.get("/", response_model=List[User])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_schemaless_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@users_router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_schemaless_db)):
    db_company = company_crud.get_company(db=db, company_id=user.company.id)
    if not db_company:
        raise HTTPException(
            status_code=400, detail="Company informed doesn't exists")

    db_user = crud.get_user_by_email(
        db, email=user.email, company_id=user.company.id)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@users_router.get("/me", response_model=User)
def get_logged_user(db: Session = Depends(get_schemaless_db), token: str = Depends(oauth2_scheme)):
    return crud.get_logged_in_user(db=db, token=token)


@users_router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_schemaless_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
