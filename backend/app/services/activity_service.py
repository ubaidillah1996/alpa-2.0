from sqlalchemy.orm import Session

from app.models.activity import Activity


def create_activity(
    db: Session,
    title: str,
    description: str,
    activity_type: str,
    user_id: int
):

    activity = Activity(
        title=title,
        description=description,
        activity_type=activity_type,
        user_id=user_id
    )


    db.add(activity)

    db.commit()

    db.refresh(activity)


    return activity

def get_user_activities(
    db: Session,
    user_id: int
):

    activities = db.query(Activity).filter(
        Activity.user_id == user_id
    ).order_by(
        Activity.created_at.desc()
    ).all()


    return activities