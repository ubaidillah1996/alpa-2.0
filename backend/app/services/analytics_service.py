from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.task import Task

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