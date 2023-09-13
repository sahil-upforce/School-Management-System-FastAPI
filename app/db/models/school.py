from sqlalchemy import String, Column, Text

from app.db.base_class import Base


class School(Base):
    name = Column(name="name", type_=String(100), nullable=False)
    address = Column(name="address", type_=Text, nullable=False)
