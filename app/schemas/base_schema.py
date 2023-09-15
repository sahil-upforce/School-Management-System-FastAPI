from pydantic import UUID4, BaseModel


class BaseSchema(BaseModel):
    is_active: bool = True


class BaseSchemaWithID:
    id: UUID4
