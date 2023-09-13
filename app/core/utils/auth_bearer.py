from datetime import datetime, timedelta

from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from pydantic import UUID4

from app.core.config import settings

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
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        return AccessToken.get_encoded_token(user_id=user_id, expire_minutes=expires_delta)

    @staticmethod
    def create_refresh_token(user_id: UUID4):
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
        return AccessToken.get_encoded_token(user_id=user_id, expire_minutes=expires_delta)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    @staticmethod
    def verify_jwt(jwt_token: str) -> bool:
        is_token_valid: bool = False
        try:
            payload = JWTBearer.decode_jwt(jwt_token)
        except Exception as e:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid

    @staticmethod
    def decode_jwt(jwt_token: str):
        try:
            payload = jwt.decode(jwt_token, SECRET_KEY, ALGORITHM)
            return payload
        except Exception as e:
            return None


jwt_bearer = JWTBearer()
