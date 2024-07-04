from sqlalchemy.orm import Session
from typing import List
from app.core.users.models import User as DomainUser

from app.core.users.ports.repository import UserRepository
from app.adapters.database.models.user_models import User as DBUser


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> DomainUser:
        db_user = self.db.query(DBUser).filter(DBUser.email == email).first()
        return DomainUser.from_orm(db_user) if db_user else None

    def create_user(self, user: DomainUser) -> DomainUser:
        db_user = DBUser(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return DomainUser.from_orm(db_user)
