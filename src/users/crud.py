from sqlalchemy.orm import Session

from src.users.models import User
from src.users.schemas import UserCreate


def get_logged_in_user(db: Session, token: str):
    return db.query(User).filter(User.token == token).first()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str, company_id: int):
    return db.query(User).filter(User.email == email and User.company_id == company_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
