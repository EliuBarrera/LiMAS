"""Interfaz del repositorio de Resource."""
from abc import ABC, abstractmethod
from uuid import UUID

from domain.resource.entities.resource import Resource


class ResourceRepository(ABC):
    @abstractmethod
    def save(self, resource: Resource) -> None: ...

    @abstractmethod
    def get_by_id(self, resource_id: UUID) -> Resource | None: ...

    @abstractmethod
    def list_all(self) -> list[Resource]: ...

    @abstractmethod
    def delete(self, resource_id: UUID) -> None: ...
