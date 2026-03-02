"""
Database models package
Import all models here to ensure they are registered with SQLAlchemy Base
"""
from app.database import Base

# Import your models here as you create them
# Example:
# from app.models.user import User
# from app.models.claim import Claim

__all__ = ["Base"]
