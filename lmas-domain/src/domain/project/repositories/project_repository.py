"""Interfaz del repositorio de Project."""
from abc import ABC, abstractmethod
from uuid import UUID

from domain.project.entities.project import Project


class ProjectRepository(ABC):
    @abstractmethod
    def save(self, project: Project) -> None: ...

    @abstractmethod
    def get_by_id(self, project_id: UUID) -> Project | None: ...

    @abstractmethod
    def list_by_user(self, user_id: UUID) -> list[Project]: ...

    @abstractmethod
    def delete(self, project_id: UUID) -> None: ...
