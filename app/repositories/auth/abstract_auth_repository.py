from abc import ABC, abstractmethod
from fastapi import HTTPException
from app.schemas.auth import TokenData


class AbstractAuthRepository(ABC):
    @abstractmethod
    def create_access_token(self, data: dict) -> str:
        pass

    @abstractmethod
    def verify_access_token(self, token: str, credentials_exception: HTTPException) -> TokenData:
        pass
