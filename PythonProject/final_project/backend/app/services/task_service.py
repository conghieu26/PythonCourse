from sqlalchemy.orm import Session

from ..model.task import Task


def list_tasks(db: Session):
    return db.query(Task).order_by(Task.created_at.desc()).all()


def create_task(db: Session, data):
    task = Task(
        title=data.title,
        description=data.description,
        priority=data.priority,
        due_date=data.due_date,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, task_id: int, data):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    for field in ("title", "description", "priority", "completed", "due_date"):
        value = getattr(data, field, None)
        if value is not None:
            setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False

    db.delete(task)
    db.commit()
    return True
