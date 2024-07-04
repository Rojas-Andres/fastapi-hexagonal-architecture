from .models import User
from .ports.repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user: User) -> User:
        return self.user_repo.create_user(user)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repo.get_user_by_email(email)