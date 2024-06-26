from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import user as user_model

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class AbstractUserRepository(ABC):
    @abstractmethod
    def get_current_user(self, token: str = Depends(oauth2_scheme),
                         db: Session = Depends(get_db)) -> user_model.User | None:
        pass

