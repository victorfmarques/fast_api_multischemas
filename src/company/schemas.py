from pydantic import BaseModel


class CompanyBase(BaseModel):
    id: int


class CompanyCreate(BaseModel):
    name: str


class CompanySchema(CompanyBase):
    schema_name: str


class Company(CompanyBase, CompanyCreate):

    class Config:
        orm_mode = True
