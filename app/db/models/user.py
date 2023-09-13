from sqlalchemy import Boolean, Column, DateTime, String, Text, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    first_name = Column(name="first_name", type_=String(100), nullable=False)
    last_name = Column(name="last_name", type_=String(100), nullable=False)
    username = Column(name="username", type_=String(100), nullable=False, unique=True, index=True)
    password = Column(name="password", type_=String, nullable=False)
    date_of_birth = Column(name="date_of_birth", type_=DateTime, nullable=False)
    gender = Column(name="gender", type_=String, nullable=False)
    email = Column(name="email", type_=String, unique=True, nullable=False, index=True)
    phone = Column(name="phone", type_=String(15), unique=True, nullable=True, index=True)
    address = Column(name="address", type_=Text, nullable=True)
    is_superuser = Column(name="is_superuser", type_=Boolean, default=False, nullable=False)

    token = relationship("Token", uselist=False, back_populates="user")


class Token(Base):
    access_token = Column(name="access_token", type_=String, nullable=False)
    refresh_token = Column(name="refresh_token", type_=String, nullable=False)

    user_id = Column(Uuid, ForeignKey("user.id"))
    user = relationship("User", back_populates="token")
