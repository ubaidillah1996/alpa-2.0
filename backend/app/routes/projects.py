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

from fastapi import HTTPException
from app.services import project_service
from app.services import analytics_service
from app.services import intelligence_service

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post(
    "/",
    response_model=ProjectResponse
)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = project_service.create_project(
        db=db,
        title=project_data.title,
        description=project_data.description,
        owner_id=current_user.id
    )

    return project

@router.get(
    "/{project_id}/progress"
)
def get_project_progress(

    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    progress = analytics_service.get_project_progress(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )

    if not progress:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return progress

@router.get(
    "/{project_id}/summary"
)
def get_project_summary(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    summary = analytics_service.get_project_summary(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )


    if not summary:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )


    return summary

@router.get(
    "/{project_id}/insight"
)
def get_project_insight(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    summary = analytics_service.get_project_summary(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )


    if not summary:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )


    insight = intelligence_service.generate_project_insight(
        summary
    )


    return insight

@router.get(
    "/{project_id}/score"
)
def get_project_score(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    summary = analytics_service.get_project_summary(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )


    if not summary:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )


    score = intelligence_service.calculate_productivity_score(
        summary
    )


    return {
        "project_id": project_id,
        **score
    }

@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = project_service.get_project(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )

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

    project = project_service.update_project(
        db=db,
        project_id=project_id,
        owner_id=current_user.id,
        title=project_data.title,
        description=project_data.description
    )


    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )


    return project

@router.delete(
    "/{project_id}"
)

def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = project_service.delete_project(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project deleted successfully"
    }

@router.get(
    "/",
    response_model=list[ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    projects = db.query(Project).filter(
        Project.owner_id == current_user.id
    ).all()


    return projects