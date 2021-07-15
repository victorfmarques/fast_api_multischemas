import os
import databases
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema


def get_database_url():
    host = os.getenv("DB_HOST", 'localhost')
    port = os.getenv("DB_PORT", '5432')
    db = os.getenv("DB_NAME", 'ooooooo')
    user = os.getenv("DB_USER", 'postgres')
    password = os.getenv("DB_PASSWORD", 'postgres')
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


database = databases.Database(get_database_url())

engine = create_engine(
    get_database_url(),
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Base.metadata.create_all(engine)


def create_schema(schema_name: str):
    if not engine.dialect.has_schema(engine, schema_name):
        engine.execute(CreateSchema(schema_name))
        return True


def create_tables(schema_name: str):
    from src.items.models import Item

    if (
        engine.dialect.has_schema(engine, schema_name) and
        not inspect(engine).has_table(engine, str(Item.__table__.name))
    ):
        Item.__table__.schema = schema_name
        Item.__table__.create(engine)
        return True
