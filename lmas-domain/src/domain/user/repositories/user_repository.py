"""Interfaz del repositorio de User. La implementación concreta vive en Infrastructure."""
from abc import ABC, abstractmethod
from uuid import UUID

from domain.user.entities.user import User
from domain.user.value_objects.email import Email


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None: ...

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None: ...

    @abstractmethod
    def get_by_email(self, email: Email) -> User | None: ...

    @abstractmethod
    def delete(self, user_id: UUID) -> None: ...
