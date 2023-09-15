import re
from datetime import datetime

from pydantic import BaseModel, EmailStr, UUID4, field_validator

from app.db.models.user import User


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: EmailStr
    phone: str = None
    user_type: str
    date_of_birth: datetime
    gender: str
    address: str = None

    @field_validator("phone")
    def validate_phone_number(cls, value: str):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if not re.search(regex, value, re.I):
            raise ValueError("Invalid phone number format")
        return value

    @field_validator("gender")
    def validate_gender(cls, value: str):
        genders = ["male", "female"]
        value = value.lower()
        if value not in genders:
            raise ValueError(f"Gender value should be {' or '.join(genders)}")
        return value

    @field_validator("user_type")
    def validate_user_type(cls, value: str):
        user_types = User.user_type_as_dict.values()
        if value not in user_types:
            raise ValueError(f"User type should be {' or '.join(user_types)}")
        return value


class UserSchema(UserBaseSchema):
    id: UUID4
    is_active: bool


class UserCreateSchema(UserBaseSchema):
    pass
