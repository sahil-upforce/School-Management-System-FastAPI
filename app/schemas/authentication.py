from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class TokenBaseSchema(BaseModel):
    user_id: str
    is_active: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenCreateSchema(TokenBaseSchema):
    pass
