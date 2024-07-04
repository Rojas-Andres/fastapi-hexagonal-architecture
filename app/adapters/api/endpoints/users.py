from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.users.models import User
from app.core.users.services import UserService
from app.adapters.database.repository.user_repository import SQLAlchemyUserRepository
from app.adapters.api.dependencies import get_db

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    user_repo = SQLAlchemyUserRepository(db)
    return UserService(user_repo)

@router.post("/users/", response_model=User)
def create_user(user: User, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user)