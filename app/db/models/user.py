from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    USER_TYPE = (
        ("STUDENT", "student"),
        ("TEACHER", "teacher"),
        ("PRINCIPAL", "principal"),
        ("SUPER_USER", "super_user"),
    )
    user_type_as_dict = dict(USER_TYPE)

    first_name = Column(name="first_name", type_=String(100), nullable=False)
    last_name = Column(name="last_name", type_=String(100), nullable=False)
    username = Column(
        name="username", type_=String(100), nullable=False, unique=True, index=True
    )
    password = Column(name="password", type_=String, nullable=False)
    user_type = Column(
        name="user_type",
        type_=String,
        nullable=False,
        default=user_type_as_dict.get("STUDENT"),
    )
    date_of_birth = Column(name="date_of_birth", type_=DateTime, nullable=False)
    gender = Column(name="gender", type_=String, nullable=False)
    email = Column(name="email", type_=String, unique=True, nullable=False, index=True)
    phone = Column(
        name="phone", type_=String(15), unique=True, nullable=True, index=True
    )
    address = Column(name="address", type_=Text, nullable=True)

    token = relationship("Token", uselist=False, back_populates="user")
    user_permissions = relationship("Permission", uselist=False, back_populates="user")
