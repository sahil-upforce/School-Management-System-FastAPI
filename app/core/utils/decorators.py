from functools import wraps

from jose import jwt

from app.core.config import settings
from app.db.managers.user_manager import TokenManager
from app.db.models.user import Token

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access_token, db = kwargs['dependencies'], kwargs['session']
        payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
        user_id = payload['sub']
        token = TokenManager.filter_by_user_id_and_access_token(
            model=Token, user_id=user_id, access_token=access_token, db=db
        )
        if token:
            return func(kwargs['dependencies'], kwargs['session'])
        else:
            return {'msg': "Token blocked"}
    return wrapper
