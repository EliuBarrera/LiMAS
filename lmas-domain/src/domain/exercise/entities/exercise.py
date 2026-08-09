"""Exercise: ejercicio de programación (ej: Two Sum, Valid Parentheses)."""
from uuid import UUID

from domain.shared.entity import AggregateRoot
from domain.shared.exceptions import InvalidValueError
from domain.exercise.value_objects.difficulty import Difficulty


class Exercise(AggregateRoot):
    def __init__(
        self,
        title: str,
        platform: str,
        difficulty: Difficulty,
        url: str = "",
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not title or not title.strip():
            raise InvalidValueError("El título del ejercicio no puede estar vacío.")
        self._title = title.strip()
        self._platform = platform
        self._difficulty = difficulty
        self._url = url

    @property
    def title(self) -> str:
        return self._title

    @property
    def platform(self) -> str:
        return self._platform

    @property
    def difficulty(self) -> Difficulty:
        return self._difficulty

    @property
    def url(self) -> str:
        return self._url
