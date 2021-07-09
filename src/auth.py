from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.database import SessionLocal
from sqlalchemy.orm import Session

from src.users.models import User
from src.company.models import Company


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_public_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print('Error: ' + str(e))
    finally:
        db.close()


def retrieve_user_by_token(db: Session = Depends(get_public_db), token: str = Depends(oauth2_scheme)):
    try:
        user = db.query(User).filter(User.token == token).first()
        return user
    except Exception as e:
        print(e)
        return None


def get_current_user(user: User = Depends(retrieve_user_by_token)):
    return user


def get_current_company_schema(user: User = Depends(get_current_user)):
    return user.company.schema_name


def get_schemaless_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print('Error: ' + str(e))
    finally:
        db.close()


def get_db(company_schema: str = Depends(get_current_company_schema)):
    db = SessionLocal()
    if company_schema:
        db.connection(
            execution_options={
                "schema_translate_map": {None: company_schema}
            }
        )
    else:
        db.connection()

    try:
        yield db
    except Exception as e:
        print('Error: ' + str(e))
    finally:
        db.close()
