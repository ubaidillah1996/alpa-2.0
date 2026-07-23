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

from app.services import task_service

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


    task = task_service.create_task(
        db=db,
        project_id=project_id,
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority
    )

    return task

@router.get(
    "/{project_id}/tasks",
    response_model=list[TaskResponse]
)
def get_project_tasks(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    tasks = task_service.get_project_tasks(
        db=db,
        project_id=project_id
    )

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

    task = task_service.update_task(
        db=db,
        task_id=task_id,
        project_id=project_id,
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,
        status=task_data.status
    )


    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


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

    task = task_service.delete_task(
        db=db,
        task_id=task_id,
        project_id=project_id
    )


    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


    return {
        "message": "Task deleted successfully"
    }