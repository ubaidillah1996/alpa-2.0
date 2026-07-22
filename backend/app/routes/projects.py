from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.project import Project
from app.models.user import User

from app.schemas.project import (
    ProjectCreate,
    ProjectResponse
)

from app.core.dependencies import get_current_user
from typing import List


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