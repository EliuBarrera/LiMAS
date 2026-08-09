"""
Phase: agrupa temas dentro de un Roadmap (ej: Lógica, Estructuras de Datos).

Es una entidad hija dentro del agregado Roadmap. Solo guarda los IDs de los
LearningTopic que pertenecen a ella; el LearningTopic completo vive en su
propio agregado (contexto `learning`).
"""
from uuid import UUID

from domain.shared.entity import Entity
from domain.shared.exceptions import InvalidValueError


class Phase(Entity):
    def __init__(
        self,
        name: str,
        order: int,
        description: str = "",
        topic_ids: list[UUID] | None = None,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        self._name = self._validate_name(name)
        self._description = description
        self._order = order
        self._topic_ids: list[UUID] = topic_ids or []

    @staticmethod
    def _validate_name(name: str) -> str:
        if not name or not name.strip():
            raise InvalidValueError("El nombre de la fase no puede estar vacío.")
        return name.strip()

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def order(self) -> int:
        return self._order

    @property
    def topic_ids(self) -> list[UUID]:
        return list(self._topic_ids)

    def link_topic(self, topic_id: UUID) -> None:
        if topic_id not in self._topic_ids:
            self._topic_ids.append(topic_id)

    def unlink_topic(self, topic_id: UUID) -> None:
        if topic_id in self._topic_ids:
            self._topic_ids.remove(topic_id)

    def reorder(self, new_order: int) -> None:
        if new_order < 0:
            raise InvalidValueError("El orden de una fase no puede ser negativo.")
        self._order = new_order
