from abc import ABC, abstractmethod
from ..models import User

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass
    
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass