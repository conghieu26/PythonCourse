from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.database import SessionLocal
from ..schemas.task import TaskCreate, TaskResponse, TaskUpdate
from ..services.task_service import create_task, delete_task, list_tasks, update_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return list_tasks(db)


@router.post("/", response_model=TaskResponse)
def create(data: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, data)


@router.patch("/{task_id}", response_model=TaskResponse)
def update(task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):
    task = update_task(db, task_id, data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}")
def remove(task_id: int, db: Session = Depends(get_db)):
    if not delete_task(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "deleted"}
