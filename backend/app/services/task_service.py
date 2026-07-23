from sqlalchemy.orm import Session

from app.models.task import Task
from app.models.project import Project


def create_task(
    db: Session,
    project_id: int,
    title: str,
    description: str,
    priority: str
):

    task = Task(
        title=title,
        description=description,
        priority=priority,
        project_id=project_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def get_project_tasks(
    db: Session,
    project_id: int
):

    tasks = db.query(Task).filter(
        Task.project_id == project_id
    ).all()

    return tasks

def update_task(
    db: Session,
    task_id: int,
    project_id: int,
    title: str,
    description: str,
    priority: str,
    status: str
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.project_id == project_id
    ).first()


    if not task:
        return None


    task.title = title
    task.description = description
    task.priority = priority
    task.status = status


    db.commit()
    db.refresh(task)


    return task

def delete_task(
    db: Session,
    task_id: int,
    project_id: int
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.project_id == project_id
    ).first()


    if not task:
        return None


    db.delete(task)

    db.commit()


    return task