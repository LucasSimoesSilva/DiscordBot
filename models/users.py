from sqlalchemy import Column, Integer, String, Date
from util.db_session import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    date = Column(Date, nullable=False)
