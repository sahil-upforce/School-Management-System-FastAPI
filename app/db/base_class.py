import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Uuid
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id = Column(name="id", type_=Uuid, primary_key=True, default=uuid.uuid4)
    created_at = Column(name="created_at", type_=DateTime, default=datetime.utcnow)
    updated_at = Column(
        name="updated_at",
        type_=DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    is_active = Column(name="is_active", type_=Boolean, default=True)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}: {self.__class__.__name__} object({self.id})>"
        )
