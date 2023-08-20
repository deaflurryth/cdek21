from sqlalchemy import Column, Integer, String

from app.database import Base


class Email_form(Base):
    __tablename__ = "email"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone = Column(String)