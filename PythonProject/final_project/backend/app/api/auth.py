from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.security import create_token
from ..db.database import SessionLocal
from ..schemas.auth import Login
from ..services.user_service import authenticate

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(data: Login, db: Session = Depends(get_db)):
    user = authenticate(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_token({"sub": user.email})
    return {"access_token": token}
