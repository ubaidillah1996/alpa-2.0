from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app.database.connection import get_db

from app.schemas.activity import (
    ActivityCreate,
    ActivityResponse
)

from app.models.user import User

from app.services import activity_service

from app.core.dependencies import get_current_user

from app.services import analytics_service

router = APIRouter(
    prefix="/activities",
    tags=["Activities"]
)


@router.post(
    "/",
    response_model=ActivityResponse
)
def create_activity(
    activity_data: ActivityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    activity = activity_service.create_activity(
        db=db,
        title=activity_data.title,
        description=activity_data.description,
        activity_type=activity_data.activity_type,
        user_id=current_user.id
    )


    return activity



@router.get(
    "/",
    response_model=list[ActivityResponse]
)
def get_activities(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    activities = activity_service.get_user_activities(
        db=db,
        user_id=current_user.id
    )


    return activities

@router.get(
    "/summary"
)
def get_activity_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    summary = analytics_service.get_activity_summary(
        db=db,
        user_id=current_user.id
    )

    return summary