from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.task import Task
from app.models.activity import Activity

def get_project_progress(
    db: Session,
    project_id: int,
    owner_id: int
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == owner_id
    ).first()


    if not project:
        return None


    tasks = db.query(Task).filter(
        Task.project_id == project_id
    ).all()


    total_tasks = len(tasks)

    completed_tasks = len([
        task for task in tasks
        if task.status == "completed"
    ])

    pending_tasks = total_tasks - completed_tasks


    progress = 0

    if total_tasks > 0:
        progress = round(
            (completed_tasks / total_tasks) * 100
        )


    return {
        "project_id": project_id,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "progress": progress
    }


def get_project_summary(
    db: Session,
    project_id: int,
    owner_id: int
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == owner_id
    ).first()


    if not project:
        return None


    tasks = db.query(Task).filter(
        Task.project_id == project_id
    ).all()


    total_tasks = len(tasks)


    completed_tasks = len([
        task for task in tasks
        if task.status == "completed"
    ])


    pending_tasks = len([
        task for task in tasks
        if task.status == "pending"
    ])


    high_priority_tasks = len([
        task for task in tasks
        if task.priority == "high"
    ])


    medium_priority_tasks = len([
        task for task in tasks
        if task.priority == "medium"
    ])


    low_priority_tasks = len([
        task for task in tasks
        if task.priority == "low"
    ])


    progress = 0

    if total_tasks > 0:
        progress = round(
            (completed_tasks / total_tasks) * 100
        )


    return {
        "project_id": project.id,
        "project_title": project.title,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "high_priority_tasks": high_priority_tasks,
        "medium_priority_tasks": medium_priority_tasks,
        "low_priority_tasks": low_priority_tasks,
        "progress": progress
    }

def get_task_analytics(
    db: Session,
    project_id: int,
    owner_id: int
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == owner_id
    ).first()


    if not project:
        return None


    tasks = db.query(Task).filter(
        Task.project_id == project_id
    ).all()


    total_tasks = len(tasks)


    completed_tasks = len([
        task for task in tasks
        if task.status == "completed"
    ])


    pending_tasks = len([
        task for task in tasks
        if task.status == "pending"
    ])


    high_priority_tasks = len([
        task for task in tasks
        if task.priority == "high"
    ])


    medium_priority_tasks = len([
        task for task in tasks
        if task.priority == "medium"
    ])


    low_priority_tasks = len([
        task for task in tasks
        if task.priority == "low"
    ])


    completion_rate = 0

    if total_tasks > 0:
        completion_rate = round(
            (completed_tasks / total_tasks) * 100
        )


    return {
        "project_id": project.id,
        "project_title": project.title,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_rate": completion_rate,
        "priority": {
            "high": high_priority_tasks,
            "medium": medium_priority_tasks,
            "low": low_priority_tasks
        }
    }

def get_activity_summary(
    db: Session,
    user_id: int
):

    activities = db.query(Activity).filter(
        Activity.user_id == user_id
    ).all()


    total_activities = len(activities)


    coding_count = len([
        activity for activity in activities
        if activity.activity_type == "coding"
    ])


    learning_count = len([
        activity for activity in activities
        if activity.activity_type == "learning"
    ])


    planning_count = len([
        activity for activity in activities
        if activity.activity_type == "planning"
    ])


    review_count = len([
        activity for activity in activities
        if activity.activity_type == "review"
    ])


    activity_counts = {
        "coding": coding_count,
        "learning": learning_count,
        "planning": planning_count,
        "review": review_count
    }


    most_active_type = "none"

    if total_activities > 0:
        most_active_type = max(
            activity_counts,
            key=activity_counts.get
        )


    return {
        "total_activities": total_activities,
        "coding": coding_count,
        "learning": learning_count,
        "planning": planning_count,
        "review": review_count,
        "most_active_type": most_active_type
    }

    