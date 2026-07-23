from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database.connection import Base


class Activity(Base):

    __tablename__ = "activities"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    title = Column(
        String,
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    activity_type = Column(
        String,
        nullable=False
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )