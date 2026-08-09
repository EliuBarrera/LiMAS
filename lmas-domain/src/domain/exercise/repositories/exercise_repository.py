"""Interfaz del repositorio de Exercise."""
from abc import ABC, abstractmethod
from uuid import UUID

from domain.exercise.entities.exercise import Exercise


class ExerciseRepository(ABC):
    @abstractmethod
    def save(self, exercise: Exercise) -> None: ...

    @abstractmethod
    def get_by_id(self, exercise_id: UUID) -> Exercise | None: ...

    @abstractmethod
    def list_by_platform(self, platform: str) -> list[Exercise]: ...

    @abstractmethod
    def delete(self, exercise_id: UUID) -> None: ...
