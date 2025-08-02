# backend/app/schemas/user.py

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Properties to receive via API on user creation
class UserCreate(BaseModel):
    email: EmailStr
    google_id: str
    full_name: str
    profile_picture_url: Optional[str] = None

# Properties to return to client
class User(BaseModel):
    id: int
    email: EmailStr
    google_id: str
    full_name: str
    profile_picture_url: Optional[str] = None
    is_active: bool
    created_at: datetime

    class Config:
        # This tells Pydantic to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str