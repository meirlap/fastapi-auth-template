# backend/app/models/user.py

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    google_id = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    profile_picture_url = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    is_active = Column(Boolean, default=True)