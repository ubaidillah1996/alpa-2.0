from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.task import Task
from app.models.project import Project
from app.models.user import User

from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskUpdate
)

from app.core.dependencies import get_current_user
from typing import List


router = APIRouter(
    prefix="/projects",
    tags=["Tasks"]
)

@router.post(
    "/{project_id}/tasks",
    response_model=TaskResponse
)
def create_task(
    project_id: int,
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()


    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )


    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,
        project_id=project.id
    )


    db.add(new_task)

    db.commit()

    db.refresh(new_task)


    return new_task

@router.get(
    "/{project_id}/tasks",
    response_model=list[TaskResponse]
)
def get_project_tasks(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()


    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )


    tasks = db.query(Task).filter(
        Task.project_id == project_id
    ).all()


    return tasks

@router.put(
    "/{project_id}/tasks/{task_id}",
    response_model=TaskResponse
)

def update_task(
    project_id: int,
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    task = db.query(Task).join(Project).filter(
        Task.id == task_id,
        Project.owner_id == current_user.id
    ).first()


    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


    if task_data.title is not None:
        task.title = task_data.title

    if task_data.description is not None:
        task.description = task_data.description

    if task_data.status is not None:
        task.status = task_data.status

    if task_data.priority is not None:
        task.priority = task_data.priority


    db.commit()
    db.refresh(task)


    return task

@router.delete(
    "/{project_id}/tasks/{task_id}"
)
def delete_task(
    project_id: int,
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).join(Project).filter(
        Task.id == task_id,
        Task.project_id == project_id,
        Project.owner_id == current_user.id
    ).first()


    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


    db.delete(task)
    db.commit()


    return {
        "message": "Task deleted successfully"
    }