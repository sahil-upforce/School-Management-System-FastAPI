from fastadmin import fastapi_app as admin_app
from fastapi import FastAPI

from app.apis.base import api_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine


def include_router(fastapi_app):
    fastapi_app.mount("/admin", admin_app)
    fastapi_app.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    fastapi_app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        debug=settings.DEBUG,
    )
    include_router(fastapi_app)
    create_tables()
    return fastapi_app


app = start_application()
