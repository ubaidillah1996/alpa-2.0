from pydantic import BaseModel

from datetime import datetime


class ActivityCreate(BaseModel):

    title: str

    description: str | None = None

    activity_type: str



class ActivityResponse(BaseModel):

    id: int

    title: str

    description: str | None

    activity_type: str

    user_id: int

    created_at: datetime


    class Config:
        from_attributes = True