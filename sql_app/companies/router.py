from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from sql_app.companies.schemas import Company, CompanyCreate
from sql_app.companies.crud import get_companies, get_company_by_name, create_company
from sql_app.auth import get_db, get_schemaless_db

companies_router = APIRouter(
    prefix="/companies",
    tags=["companies"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@companies_router.post("/", response_model=Company)
def create_company(company: CompanyCreate, db: Session = Depends(get_schemaless_db)):
    db_company = get_company_by_name(db, name=company.name)
    if db_company:
        raise HTTPException(
            status_code=400, detail="A Company with this name has already been registered")
    return create_company(db=db, company=company)


@companies_router.get("/", response_model=List[Company])
def list_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_schemaless_db)):
    items = get_companies(db, skip=skip, limit=limit)
    return items


@companies_router.get("/{company_id}", response_model=Company)
def retrieve_company(company_id: int, db: Session = Depends(get_schemaless_db)):
    db_company = get_companies(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company
