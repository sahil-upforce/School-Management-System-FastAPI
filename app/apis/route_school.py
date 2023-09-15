from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.core.utils.auth_bearer import jwt_bearer
from app.core.utils.permissions import PermissionChecker
from app.db.session import get_db
from app.schemas.school import SchoolCreateSchema, SchoolSchema, SchoolUpdateSchema
from app.services.school import SchoolService


school_router = APIRouter()


@school_router.post(path="/", dependencies=[Depends(jwt_bearer)], response_model=SchoolSchema)
def create_school(school: SchoolCreateSchema, db: Session = Depends(get_db), authorized: bool = Depends(PermissionChecker(required_permissions=["school: create"]))):
    school = SchoolService.create(school_schema=school, db=db)
    return school


@school_router.get(path="/", dependencies=[Depends(jwt_bearer)], response_model=List[SchoolSchema])
def fetch_all_schools(db: Session = Depends(get_db), authorized: bool = Depends(PermissionChecker(required_permissions=["school: read"]))):
    schools = SchoolService.fetch_all(db=db)
    return schools


@school_router.get(path="/{school_id}", dependencies=[Depends(jwt_bearer)], response_model=SchoolSchema)
def get_school_details(school_id: UUID4, db: Session = Depends(get_db),authorized: bool = Depends(PermissionChecker(required_permissions=["school: read"]))):
    school = SchoolService.get_school(school_id=school_id, db=db)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return school


@school_router.put(path="/{school_id}", dependencies=[Depends(jwt_bearer)], response_model=SchoolSchema)
def update_school(school_id: UUID4, school: SchoolUpdateSchema, db: Session = Depends(get_db),authorized: bool = Depends(PermissionChecker(required_permissions=["school: change"]))):
    school = SchoolService.update_school(school_id=school_id, school_schema=school, db=db)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return school


@school_router.delete(path="/{school_id}", dependencies=[Depends(jwt_bearer)])
def delete_school(school_id: UUID4, db: Session = Depends(get_db), authorized: bool = Depends(PermissionChecker(required_permissions=["school: delete"]))):
    school = SchoolService.delete_school(school_id=school_id, db=db)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return JSONResponse(content={"detail": f"School {school.id} is deleted"}, status_code=200)
