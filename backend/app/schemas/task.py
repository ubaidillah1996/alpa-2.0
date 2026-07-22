from pydantic import BaseModel
from datetime import datetime


class TaskCreate(BaseModel):

    title: str

    description: str | None = None

    priority: str = "medium"



class TaskUpdate(BaseModel):

    title: str | None = None

    description: str | None = None

    status: str | None = None

    priority: str | None = None



class TaskResponse(BaseModel):

    id: int

    title: str

    description: str | None

    status: str

    priority: str

    project_id: int

    created_at: datetime


    class Config:
        from_attributes = True