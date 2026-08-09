"""StudyRecord: registro de una sesión de estudio sobre un tema, en una fecha determinada."""
from datetime import date as date_type
from uuid import UUID

from domain.shared.entity import Entity
from domain.shared.exceptions import InvalidValueError
from domain.learning.value_objects.duration import Duration


class StudyRecord(Entity):
    def __init__(
        self,
        date: date_type,
        duration: Duration,
        energy: int | None = None,
        concentration: int | None = None,
        notes: str = "",
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        self._date = date
        self._duration = duration
        self._energy = self._validate_scale(energy, "energía")
        self._concentration = self._validate_scale(concentration, "concentración")
        self._notes = notes

    @staticmethod
    def _validate_scale(value: int | None, field_name: str) -> int | None:
        if value is not None and not (1 <= value <= 5):
            raise InvalidValueError(f"El valor de {field_name} debe estar entre 1 y 5.")
        return value

    @property
    def date(self) -> date_type:
        return self._date

    @property
    def duration(self) -> Duration:
        return self._duration

    @property
    def energy(self) -> int | None:
        return self._energy

    @property
    def concentration(self) -> int | None:
        return self._concentration

    @property
    def notes(self) -> str:
        return self._notes
