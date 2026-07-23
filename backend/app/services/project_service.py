from sqlalchemy.orm import Session

from app.models.project import Project

from app.models.task import Task


def create_project(
    db: Session,
    title: str,
    description: str,
    owner_id: int
):

    project = Project(
        title=title,
        description=description,
        owner_id=owner_id
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project

def get_projects(
    db: Session,
    owner_id: int
):

    projects = db.query(Project).filter(
        Project.owner_id == owner_id
    ).all()

    return projects

def get_project(
    db: Session,
    project_id: int,
    owner_id: int
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == owner_id
    ).first()

    return project

def update_project(
    db: Session,
    project_id: int,
    owner_id: int,
    title: str,
    description: str
):

    print("UPDATE PROJECT DEBUG")
    print("project_id =", project_id)
    print("owner_id =", owner_id)


    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == owner_id
    ).first()


    print("found =", project)


    if not project:
        return None


    project.title = title
    project.description = description


    db.commit()
    db.refresh(project)


    return project

def delete_project(
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


    db.delete(project)

    db.commit()


    return project

# def get_project_progress(
#     db: Session,
#     project_id: int,
#     owner_id: int
# ):

#     project = db.query(Project).filter(
#         Project.id == project_id,
#         Project.owner_id == owner_id
#     ).first()


#     if not project:
#         return None


#     tasks = db.query(Task).filter(
#         Task.project_id == project_id
#     ).all()


#     total_tasks = len(tasks)

#     completed_tasks = len([
#         task for task in tasks
#         if task.status == "completed"
#     ])

#     pending_tasks = total_tasks - completed_tasks


#     progress = 0

#     if total_tasks > 0:
#         progress = round(
#             (completed_tasks / total_tasks) * 100
#         )


#     return {
#         "project_id": project_id,
#         "total_tasks": total_tasks,
#         "completed_tasks": completed_tasks,
#         "pending_tasks": pending_tasks,
#         "progress": progress
#     }