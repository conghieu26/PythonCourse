from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.database import SessionLocal
from ..schemas.user import UserCreate, UserResponse
from ..services.user_service import create_user

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create(data: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, data)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
