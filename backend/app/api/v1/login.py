# backend/app/api/v1/login.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.crud import crud_user
from app.schemas import user as user_schema
from app.core.security import create_access_token, verify_google_token
from app.database import SessionLocal

router = APIRouter()

class GoogleToken(BaseModel):
    token: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login/google", response_model=user_schema.Token)
def login_with_google(google_token: GoogleToken, db: Session = Depends(get_db)):
    idinfo = verify_google_token(google_token.token)
    if not idinfo:
        raise HTTPException(status_code=400, detail="Invalid Google token")

    email = idinfo["email"]
    user = crud_user.get_user_by_email(db, email=email)

    if not user:
        # User doesn't exist, create them
        user_in = user_schema.UserCreate(
            email=email,
            google_id=idinfo.get("sub"),
            full_name=idinfo.get("name"),
            profile_picture_url=idinfo.get("picture"),
        )
        user = crud_user.create_user(db, user=user_in)

    # Create our own access token for the user
    access_token = create_access_token(subject=user.id)
    
    return {"access_token": access_token, "token_type": "bearer"}