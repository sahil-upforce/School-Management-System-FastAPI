from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreateSchema, UserSchema
from app.services.user import UserService

user_router = APIRouter()


@user_router.post(path="/", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    user = UserService.create(user_schema=user, db=db)
    return user


@user_router.get(path="/", response_model=List[UserSchema])
def fetch_all_users(db: Session = Depends(get_db)):
    users = UserService.fetch_all(db=db)
    return users
