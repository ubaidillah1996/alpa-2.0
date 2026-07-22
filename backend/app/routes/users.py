from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def get_users():

    return {
        "message": "Users endpoint working"
    }


@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    hashed = hash_password(user.password)

    

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hashed
    )



    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "full_name": new_user.full_name,
        "email": new_user.email
    }