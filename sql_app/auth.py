from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from sql_app.database import SessionLocal
from sqlalchemy.orm import Session

from sql_app.users.models import User
from sql_app.companies.models import Company


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def retrieve_user_by_token(token: str,  db: Session):
    try:
        user = db.query(User).filter(User.token == token).first()
        return user
    except Exception as e:
        print(e)
        return None


def get_current_user(token: str = Depends(oauth2_scheme)):
    return retrieve_user_by_token(token)


def get_current_company_schema(user: User = Depends(get_current_user)):
    return Company(id=user.company).schema_name


def get_schemaless_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print('Error: ' + str(type(e)))
    finally:
        db.close()


def get_db(company_schema: str = Depends(get_current_company_schema)):
    db = SessionLocal()
    if company_schema:
        db.connection(
            execution_options={
                "schema_translate_map": {"per_user": company_schema}
            }
        )
    else:
        db.connection()

    try:
        yield db
    except Exception as e:
        print('Error: ' + str(type(e)))
    finally:
        db.close()
