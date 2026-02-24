from abc import ABC, abstractmethod
from typing import Any


class UserRepository(ABC):
    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def create(self, email: str, password: str) -> Any:
        raise NotImplementedError

