from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.utils.auth_bearer import jwt_bearer
from app.db.session import get_db
from app.schemas.authentication import LoginSchema, TokenSchema
from app.services.authentication import LoginService

authentication_router = APIRouter()


@authentication_router.post(path="/login", response_model=TokenSchema)
def login(credentials: LoginSchema, db: Session = Depends(get_db)):
    token = LoginService.login(credentials=credentials, db=db)
    return token


@authentication_router.post(path="/logout", dependencies=[Depends(jwt_bearer)])
def logout():
    return {"detail": "Logout successfully"}
