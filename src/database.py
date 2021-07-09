from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema

# SQLALCHEMY_DATABASE_URL = "sqlite:///./src.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fast_api_multischemas"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_schema(schema_name: str):
    """
        Creates a new postgres schema
        - **schema_name**: name of the new schema to create
    """
    if not engine.dialect.has_schema(engine, schema_name):
        engine.execute(CreateSchema(schema_name))
        return True


def create_tables(schema_name: str):
    """
        Create new tables for postgres schema
        - **schema_name**: schema in which tables are to be created
    """
    from src.items.models import Item

    if (
        engine.dialect.has_schema(engine, schema_name) and
        not inspect(engine).has_table(engine, str(Item.__table__.name))
    ):
        Item.__table__.schema = schema_name
        Item.__table__.create(engine)
        return True
