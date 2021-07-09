from sqlalchemy.orm import Session

from src.company.models import Company
from src.company. schemas import CompanyCreate

from src.database import create_schema, create_tables


def get_company(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()


def get_company_by_name(db: Session, name: str):
    return db.query(Company).filter(Company.name == name).first()


def get_company_by_id(db: Session, id: str):
    return db.query(Company).filter(Company.id == id).first()


def get_company(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Company).offset(skip).limit(limit).all()


def create_company(db: Session, company: CompanyCreate):
    schema_name = company.name + '_0001'
    db_company = Company(
        name=company.name, schema_name=schema_name
    )

    try:
        if (create_schema(schema_name) and create_tables(schema_name)):
            db.add(db_company)
            db.commit()
            db.refresh(db_company)
            return db_company
        raise Exception("Failed while configuring company database")
    except Exception as e:
        print(f"Error -> {str(e)}")
        return False
