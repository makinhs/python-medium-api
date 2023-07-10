from database.config import Session
from .user_entity import User
import bcrypt


def getAllUsers():
    session = Session()
    users = session.query(User).all()
    return users


def getUser(user_id: int):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    return user


def createUser(user_data: dict):
    user_data["password"] = bcrypt.hashpw(user_data["password"].encode("utf-8"), bcrypt.gensalt())

    session = Session()
    user = User(**user_data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def updateUser(user_id: int, user_data: dict):
    if(user_data["password"]):
        user_data["password"] = bcrypt.hashpw(user_data["password"].encode("utf-8"), bcrypt.gensalt())

    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in user_data.items():
            setattr(user, key, value)
        session.commit()
        session.refresh(user)
    return user


def deleteUser(user_id: int):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
    return {"message": f"Delete user with ID: {user_id}"}


def verify_password(stored_password: str, provided_password: str) -> bool:
    return bcrypt.checkpw(provided_password.encode("utf-8"), stored_password.encode("utf-8"))
