from pydantic import BaseModel, UUID4


class BaseSchema(BaseModel):
    is_active: bool = True


class BaseSchemaWithID:
    id: UUID4
