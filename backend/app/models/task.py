from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class Task(Base):

    __tablename__ = "tasks"


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


    status = Column(
        String,
        default="pending"
    )


    priority = Column(
        String,
        default="medium"
    )


    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    project = relationship(
        "Project",
        back_populates="tasks"
    )