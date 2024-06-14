from .db_connect import Base
from sqlalchemy import String, Column, Integer

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))