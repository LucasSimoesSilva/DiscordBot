from typing import Type
from sqlalchemy.orm import Session
from models.users import User
import datetime


def create_user(db: Session, name: str, date: datetime) -> User:
    user = User(name=name, date=date)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def list_users(db: Session) -> list[Type[User]]:
    return db.query(User).order_by(User.id.asc()).all()
