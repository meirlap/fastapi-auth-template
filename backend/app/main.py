# backend/app/main.py
from fastapi import FastAPI
from .core.config import settings
from .database import engine
from .models import user
# Import both endpoint files
from .api.v1 import endpoints as user_endpoints
from .api.v1 import login as login_endpoints

user.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# Include both routers
app.include_router(user_endpoints.router, prefix="/api/v1", tags=["Users"])
app.include_router(login_endpoints.router, prefix="/api/v1", tags=["Login"])

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}