from sqlalchemy import Column, Integer, String

from ..database import Base


class Company(Base):
    __tablename__ = "company"
    __table_args__ = {
        "schema": "public"
    }

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    schema_name = Column(String, nullable=False)
