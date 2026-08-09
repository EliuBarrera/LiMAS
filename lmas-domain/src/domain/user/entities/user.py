"""Entidad User: representa al estudiante dueño de todo el aprendizaje."""
from datetime import datetime
from uuid import UUID

from domain.shared.entity import AggregateRoot
from domain.shared.exceptions import InvalidValueError
from domain.user.value_objects.email import Email


class User(AggregateRoot):
    def __init__(
        self,
        name: str,
        email: Email,
        registration_date: datetime | None = None,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        self._name = self._validate_name(name)
        self._email = email
        self._registration_date = registration_date or datetime.utcnow()

    @staticmethod
    def _validate_name(name: str) -> str:
        if not name or not name.strip():
            raise InvalidValueError("El nombre del usuario no puede estar vacío.")
        return name.strip()

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> Email:
        return self._email

    @property
    def registration_date(self) -> datetime:
        return self._registration_date

    def rename(self, new_name: str) -> None:
        self._name = self._validate_name(new_name)

    def change_email(self, new_email: Email) -> None:
        self._email = new_email
