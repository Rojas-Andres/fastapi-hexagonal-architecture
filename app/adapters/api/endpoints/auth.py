from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from app.core.auth.models import Token
from app.core.auth.services import AuthService
from app.core.users.services import UserService
from app.adapters.database.repository.user_repository import SQLAlchemyUserRepository
from app.adapters.api.dependencies import get_db

from app.core.auth.models import LoginRequest
from app.core.users.models import User as UserCreate

router = APIRouter()


def get_user_service(database: Session = Depends(get_db)):
    user_repo = SQLAlchemyUserRepository(database)
    return UserService(user_repo)


def get_auth_service(user_service: UserService = Depends(get_user_service)):
    return AuthService(user_service)


@router.post("/login", response_model=Token)
def login_for_access_token(
    login_user: LoginRequest, auth_service: AuthService = Depends(get_auth_service)
):
    user = auth_service.authenticate_user(login_user.email, login_user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.create_access_token(data={"email": user.email})
    return access_token


@router.post("/signup", response_model=UserCreate)
def create_user(
    user: UserCreate, auth_service: AuthService = Depends(get_auth_service)
):
    user_exist = auth_service.user_service.get_user_by_email(user.email)
    if user_exist:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth_service.create_user(user)
