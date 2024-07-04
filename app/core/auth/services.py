from datetime import timedelta, datetime
from typing import Union
import jwt
from passlib.context import CryptContext
from .ports.repository import AuthRepository
from .models import Token
from ..users.services import UserService
from app.core.users.models import User
from app.core.auth.security import Hasher
from app.config import settings


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def authenticate_user(self, email: str, password: str) -> Union[User, None]:
        user = self.user_service.get_user_by_email(email)
        if not user or not Hasher.verify_password(password, user.password):
            return None
        return user

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return Token(access_token=encoded_jwt, token_type="bearer", email=data["email"])

    def create_user(self, user: User) -> User:
        user.password = Hasher.get_password_hash(user.password)
        return self.user_service.create_user(user)
