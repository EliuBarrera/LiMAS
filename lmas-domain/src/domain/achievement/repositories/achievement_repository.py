"""Interfaz del repositorio de Achievement."""
from abc import ABC, abstractmethod
from uuid import UUID

from domain.achievement.entities.achievement import Achievement


class AchievementRepository(ABC):
    @abstractmethod
    def save(self, achievement: Achievement) -> None: ...

    @abstractmethod
    def list_by_user(self, user_id: UUID) -> list[Achievement]: ...

    @abstractmethod
    def exists(self, user_id: UUID, name: str) -> bool:
        """Útil para no otorgar el mismo logro dos veces."""
        ...
