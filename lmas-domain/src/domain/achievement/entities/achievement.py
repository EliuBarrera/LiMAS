"""Achievement: logro desbloqueado por el usuario (ej: 100 ejercicios resueltos, 30 días consecutivos)."""
from datetime import date as date_type
from uuid import UUID

from domain.shared.entity import AggregateRoot
from domain.shared.exceptions import InvalidValueError


class Achievement(AggregateRoot):
    def __init__(
        self,
        user_id: UUID,
        name: str,
        description: str,
        date: date_type,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not name or not name.strip():
            raise InvalidValueError("El nombre del logro no puede estar vacío.")
        self._user_id = user_id
        self._name = name.strip()
        self._description = description
        self._date = date

    @property
    def user_id(self) -> UUID:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def date(self) -> date_type:
        return self._date
