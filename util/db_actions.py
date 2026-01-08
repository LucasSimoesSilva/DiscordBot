from typing import Type
from sqlalchemy.orm import Session
from models.users import User
import datetime


def user_exists(db: Session, name: str) -> bool:
    user = db.query(User).filter(User.name == name).first()
    if user:
        return True
    return False


def create_user(db: Session, name: str, date: datetime) -> Type[User] | User:
    user = User(name=name, date=date)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def list_users(db: Session) -> list[Type[User]]:
    return db.query(User).order_by(User.id.asc()).all()


def delete_user_by_name(db: Session, name: str) -> bool:
    user = db.query(User).filter(User.name == name).first()
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True

def users_by_name(db: Session):
    user_list = list_users(db)
    return {u.name: u for u in user_list}