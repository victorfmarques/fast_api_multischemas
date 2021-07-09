from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from src.company.schemas import Company, CompanyCreate
from src.company.crud import get_company, get_company_by_name, create_company
from src.auth import get_db, get_schemaless_db

company_router = APIRouter(
    prefix="/company",
    tags=["company"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@company_router.post("/", response_model=Company)
def create_company(company: CompanyCreate, db: Session = Depends(get_schemaless_db)):
    db_company = get_company_by_name(db, name=company.name)
    if db_company:
        raise HTTPException(
            status_code=400, detail="A Company with this name has already been registered")
    return create_company(db=db, company=company)


@company_router.get("/", response_model=List[Company])
def list_company(skip: int = 0, limit: int = 100, db: Session = Depends(get_schemaless_db)):
    items = get_company(db, skip=skip, limit=limit)
    return items


@company_router.get("/{company_id}", response_model=Company)
def retrieve_company(company_id: int, db: Session = Depends(get_schemaless_db)):
    db_company = get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company
