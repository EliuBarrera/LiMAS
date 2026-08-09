"""LearningObjective: objetivo concreto dentro de un LearningTopic (ej: 'Resolver 20 ejercicios')."""
from uuid import UUID

from domain.shared.entity import Entity
from domain.shared.exceptions import InvalidValueError
from domain.learning.value_objects.priority import Priority
from domain.learning.value_objects.objective_status import ObjectiveStatus


class LearningObjective(Entity):
    def __init__(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        status: ObjectiveStatus = ObjectiveStatus.PENDING,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not title or not title.strip():
            raise InvalidValueError("El título del objetivo no puede estar vacío.")
        self._title = title.strip()
        self._description = description
        self._priority = priority
        self._status = status

    @property
    def title(self) -> str:
        return self._title

    @property
    def priority(self) -> Priority:
        return self._priority

    @property
    def status(self) -> ObjectiveStatus:
        return self._status

    def start(self) -> None:
        self._status = ObjectiveStatus.IN_PROGRESS

    def complete(self) -> None:
        self._status = ObjectiveStatus.COMPLETED
