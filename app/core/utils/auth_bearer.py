from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette import status

from app.core.config import settings
from app.db.managers.user_manager import UserManager
from app.db.models.user import User
from app.db.session import get_db

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_MINUTES = settings.REFRESH_TOKEN_EXPIRE_MINUTES


class AccessToken:
    @staticmethod
    def get_encoded_token(user_id: UUID4, expire_minutes):
        to_encode = {"exp": expire_minutes, "user_id": str(user_id)}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
        return encoded_jwt

    @staticmethod
    def create_access_token(user_id: UUID4):
        expires_delta = datetime.utcnow() + timedelta(
            minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return AccessToken.get_encoded_token(
            user_id=user_id, expire_minutes=expires_delta
        )

    @staticmethod
    def create_refresh_token(user_id: UUID4):
        expires_delta = datetime.utcnow() + timedelta(
            minutes=int(REFRESH_TOKEN_EXPIRE_MINUTES)
        )
        return AccessToken.get_encoded_token(
            user_id=user_id, expire_minutes=expires_delta
        )


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme"
                )
            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token"
                )
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
        return credentials.credentials

    @staticmethod
    def verify_jwt(jwt_token: str):
        try:
            payload = JWTBearer.decode_jwt(jwt_token)
        except Exception:
            payload = None
        return payload

    @staticmethod
    def decode_jwt(jwt_token: str):
        try:
            payload = jwt.decode(jwt_token, SECRET_KEY, ALGORITHM)
            return payload
        except Exception:
            return None


jwt_bearer = JWTBearer()


def get_current_user_from_token(
    token: str = Depends(jwt_bearer), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    payload = JWTBearer.decode_jwt(jwt_token=token)
    user_id: str = payload.get("user_id")
    if user_id is None:
        raise credentials_exception
    user = UserManager.get_by_id(model=User, obj_id=user_id, db=db)
    if user is None:
        raise credentials_exception
    return user
