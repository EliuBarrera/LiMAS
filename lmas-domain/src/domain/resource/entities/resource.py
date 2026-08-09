"""Resource: material utilizado durante el estudio (libro, video, curso, etc.)."""
from uuid import UUID

from domain.shared.entity import AggregateRoot
from domain.shared.exceptions import InvalidValueError
from domain.resource.value_objects.resource_type import ResourceType


class Resource(AggregateRoot):
    def __init__(
        self,
        name: str,
        type: ResourceType,
        url: str = "",
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not name or not name.strip():
            raise InvalidValueError("El nombre del recurso no puede estar vacío.")
        self._name = name.strip()
        self._type = type
        self._url = url

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> ResourceType:
        return self._type

    @property
    def url(self) -> str:
        return self._url
