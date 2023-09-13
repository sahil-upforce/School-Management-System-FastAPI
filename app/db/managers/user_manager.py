from sqlalchemy.orm import Session

from app.db.managers.base_manager import BaseManager
from app.db.models.user import User


class UserManager(BaseManager):
    @staticmethod
    def create(model, data, db: Session):
        UserManager.check_conflicts(data=data, db=db)
        return super(UserManager, UserManager).create(model=model, data=data, db=db)

    @staticmethod
    def get_by_email(model, email, db: Session):
        return db.query(model).filter(model.email == email, model.is_active == True).first()

    @staticmethod
    def get_by_username(model, username, db: Session):
        return db.query(model).filter(model.username == username, model.is_active == True).first()

    @staticmethod
    def get_by_phone(model, phone, db: Session):
        return db.query(model).filter(model.phone == phone, model.is_active == True).first()

    @staticmethod
    def check_conflicts(data: dict, db: Session):
        UserManager.check_username_is_already_exists(username=data.get("username"), db=db)
        UserManager.check_email_is_already_exists(email=data.get("email"), db=db)
        UserManager.check_phone_is_already_exists(phone=data.get("phone"), db=db)

    @staticmethod
    def check_username_is_already_exists(username: str, db: Session):
        user_obj = UserManager.get_by_username(model=User, username=username, db=db)
        if user_obj:
            raise ValueError("Username is already exists")

    @staticmethod
    def check_email_is_already_exists(email, db: Session):
        user_obj = UserManager.get_by_email(model=User, email=email, db=db)
        if user_obj:
            raise ValueError("Email is already exists")

    @staticmethod
    def check_phone_is_already_exists(phone: str, db: Session):
        if phone:
            user_obj = UserManager.get_by_phone(model=User, phone=phone, db=db)
            if user_obj:
                raise ValueError("Phone number is already exists")


class TokenManager(BaseManager):

    @staticmethod
    def filter_by_user_id_and_access_token(model, access_token, user_id, db: Session):
        return db.query(model).filter(model.access_token == access_token, model.is_active == True, model.user_id==user_id).first()
