import re
from datetime import datetime

from pydantic import BaseModel, EmailStr, UUID4, field_validator


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    gender: str
    password: str
    email: EmailStr
    phone: str = None
    date_of_birth: datetime
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


class UserSchema(UserBaseSchema):
    id: UUID4
    is_active: bool
    is_superuser: bool


class UserCreateSchema(UserBaseSchema):
    pass
