"""Interfaz del repositorio de Roadmap."""
from abc import ABC, abstractmethod
from uuid import UUID

from domain.roadmap.entities.roadmap import Roadmap


class RoadmapRepository(ABC):
    @abstractmethod
    def save(self, roadmap: Roadmap) -> None: ...

    @abstractmethod
    def get_by_id(self, roadmap_id: UUID) -> Roadmap | None: ...

    @abstractmethod
    def list_by_user(self, user_id: UUID) -> list[Roadmap]: ...

    @abstractmethod
    def delete(self, roadmap_id: UUID) -> None: ...
