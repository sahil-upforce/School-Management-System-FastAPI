from pydantic import BaseModel, UUID4


class SchoolBaseSchema(BaseModel):
    name: str
    address: str


class SchoolSchema(SchoolBaseSchema):
    id: UUID4
    is_active: bool


class SchoolCreateSchema(SchoolBaseSchema):
    pass


class SchoolUpdateSchema(SchoolBaseSchema):
    pass
