from models.user import User, user_admin
from security.jwt_manager import create_token


def login(user: User) -> str:
    token: str = ""
    if user.email == user_admin.email and user.password == user_admin.password:
        token = create_token(user.model_dump())
    return token