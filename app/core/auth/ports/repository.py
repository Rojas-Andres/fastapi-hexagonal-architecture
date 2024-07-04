from abc import ABC, abstractmethod
from ..models import Token


class AuthRepository(ABC):
    @abstractmethod
    def authenticate_user(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def create_access_token(self, data: dict) -> Token:
        pass
