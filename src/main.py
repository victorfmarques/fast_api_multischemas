from fastapi import FastAPI
from src.company.router import company_router
from src.users.router import users_router
from src.items.router import items_router
from src.database import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(company_router)
app.include_router(users_router)
app.include_router(items_router)
