from pydantic import UUID4
from sqlalchemy.orm import Session

from app.db.managers.base_manager import BaseManager
from app.db.models.school import School
from app.schemas.school import SchoolCreateSchema, SchoolUpdateSchema


class SchoolService:
    @staticmethod
    def create(school_schema: SchoolCreateSchema, db: Session):
        school = BaseManager.create(
            model=School, data=school_schema.model_dump(), db=db
        )
        return school

    @staticmethod
    def fetch_all(db: Session):
        schools = BaseManager.fetch_all(model=School, db=db)
        return schools

    @staticmethod
    def get_school(school_id: UUID4, db: Session):
        school = BaseManager.get_by_id(model=School, obj_id=school_id, db=db)
        return school

    @staticmethod
    def update_school(school_id: UUID4, school_schema: SchoolUpdateSchema, db: Session):
        school = BaseManager.update(
            model=School, obj_id=school_id, data=school_schema.model_dump(), db=db
        )
        return school

    @staticmethod
    def delete_school(school_id: UUID4, db: Session):
        school = BaseManager.delete_by_id(model=School, obj_id=school_id, db=db)
        return school
