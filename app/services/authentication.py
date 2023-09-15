from sqlalchemy.orm import Session

from app.core.utils.auth_bearer import AccessToken
from app.core.utils.hashing import Hasher
from app.db.managers.authentication_manager import TokenManager
from app.db.managers.user_manager import UserManager
from app.db.models.authentication import Token
from app.db.models.user import User
from app.schemas.authentication import LoginSchema


class LoginService:

    @staticmethod
    def login(credentials: LoginSchema, db: Session):
        data = credentials.model_dump()
        user = UserManager.get_by_email(model=User, email=data.get("email"), db=db)
        if not user:
            raise ValueError("Invalid email")

        if not Hasher.verify_password(plain_password=data.get("password"), hashed_password=user.password):
            raise ValueError("Invalid password")

        access_token = AccessToken.create_access_token(user_id=user.id)
        refresh_token = AccessToken.create_refresh_token(user_id=user.id)
        token_create_data = {"access_token": access_token, "refresh_token": refresh_token, "user_id": user.id}
        token = TokenManager.create(model=Token, data=token_create_data, db=db)
        return token
