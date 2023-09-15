from fastapi import Depends, HTTPException
from starlette import status

from app.core.utils.auth_bearer import get_current_user_from_token
from app.db.managers.user_manager import UserManager


class PermissionChecker:

    def __init__(self, required_permissions: list[str]) -> None:
        self.required_permissions = required_permissions

    def __call__(self, user=Depends(get_current_user_from_token)) -> bool:
        for r_perm in self.required_permissions:
            if r_perm not in UserManager.get_user_permissions(user):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Permissions denied'
                )
        return True
