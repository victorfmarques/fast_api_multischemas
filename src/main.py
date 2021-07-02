from fastapi import FastAPI
from src.companies.router import companies_router
from src.users.router import users_router
from src.items.router import items_router


from src.database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(companies_router)
app.include_router(users_router)
app.include_router(items_router)
