from sqlalchemy.orm import Session

from app.core.utils.hashing import Hasher
from app.db.managers.user_manager import UserManager
from app.db.models.user import User
from app.schemas.user import UserCreateSchema


class UserService:
    @staticmethod
    def create(user_schema: UserCreateSchema, db: Session):
        user_schema.password = Hasher.get_password_hash(user_schema.password)
        user = UserManager.create(model=User, data=user_schema.model_dump(), db=db)
        return user

    @staticmethod
    def fetch_all(db: Session):
        users = UserManager.fetch_all(model=User, db=db)
        return users
