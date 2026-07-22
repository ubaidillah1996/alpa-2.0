from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.project import Project
from app.models.user import User

from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate
)

from app.core.dependencies import get_current_user
from typing import List

from fastapi import HTTPException

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post(
    "/",
    response_model=ProjectResponse
)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_project = Project(
        title=project.title,
        description=project.description,
        owner_id=current_user.id
    )


    db.add(new_project)

    db.commit()

    db.refresh(new_project)


    return new_project

@router.get(
    "/",
    response_model=List[ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    projects = db.query(Project).filter(
        Project.owner_id == current_user.id
    ).all()


    return projects

@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
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


    return project

@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_project(
    project_id: int,
    project_data: ProjectUpdate,
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


    if project_data.title is not None:
        project.title = project_data.title


    if project_data.description is not None:
        project.description = project_data.description


    if project_data.status is not None:
        project.status = project_data.status


    db.commit()

    db.refresh(project)


    return project

