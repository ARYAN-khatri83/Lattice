"""
Example model - you can delete this file and create your own models
"""
from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base


class ExampleModel(Base):
    """Example model to demonstrate structure"""
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
