from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.connection import Base
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        default="member"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    projects = relationship(
    "Project",
    back_populates="owner"
    )