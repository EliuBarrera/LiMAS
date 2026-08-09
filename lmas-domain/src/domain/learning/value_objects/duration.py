"""Value Object Duration: minutos de estudio o de resolución de un ejercicio. Siempre > 0."""
from dataclasses import dataclass

from domain.shared.exceptions import InvalidValueError


@dataclass(frozen=True)
class Duration:
    minutes: int

    def __post_init__(self) -> None:
        if self.minutes <= 0:
            raise InvalidValueError("La duración debe ser mayor a 0 minutos.")

    def __add__(self, other: "Duration") -> "Duration":
        return Duration(self.minutes + other.minutes)

    def __lt__(self, other: "Duration") -> bool:
        return self.minutes < other.minutes

    def __str__(self) -> str:
        return f"{self.minutes} min"
