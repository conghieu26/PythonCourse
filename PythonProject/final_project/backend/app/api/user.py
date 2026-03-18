from fastapi import APIRouter, Depends
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
    return create_user(db, data)
