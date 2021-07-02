from fastapi import FastAPI
from sql_app.companies.router import companies_router
from sql_app.users.router import users_router
from sql_app.items.router import items_router


from sql_app.database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(companies_router)
app.include_router(users_router)
app.include_router(items_router)
