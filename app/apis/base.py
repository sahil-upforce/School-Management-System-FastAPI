from fastapi import APIRouter

from app.apis.route_authentication import authentication_router
from app.apis.route_school import school_router
from app.apis.route_user import user_router

api_router = APIRouter()

api_router.include_router(router=school_router, prefix="/schools", tags=["School"])
api_router.include_router(router=user_router, prefix="/user", tags=["User"])
api_router.include_router(router=authentication_router, prefix="/authentication", tags=["Authentication"])
