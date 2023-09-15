from sqlalchemy import Column, String, ForeignKey, Uuid
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.models.user import User


class Permission(Base):
    is_active = None
    permissions = Column(name="permissions", type_=ARRAY(String))
    user_id = Column(Uuid, ForeignKey("user.id"))
    user = relationship(User, back_populates="user_permissions")


class Token(Base):
    access_token = Column(name="access_token", type_=String, nullable=False)
    refresh_token = Column(name="refresh_token", type_=String, nullable=False)

    user_id = Column(Uuid, ForeignKey("user.id"))
    user = relationship(User, back_populates="token")
