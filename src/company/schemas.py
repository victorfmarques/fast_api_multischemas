from pydantic import BaseModel


class CompanyBase(BaseModel):
    id: int


class CompanyCreate(BaseModel):
    name: str


class Company(CompanyBase, CompanyCreate):
    token: str

    class Config:
        orm_mode = True
