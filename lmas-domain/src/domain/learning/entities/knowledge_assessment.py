"""KnowledgeAssessment: nivel de dominio autoevaluado sobre un tema, en una fecha."""
from datetime import date as date_type
from uuid import UUID

from domain.shared.entity import Entity
from domain.learning.value_objects.mastery_level import MasteryLevel


class KnowledgeAssessment(Entity):
    def __init__(
        self,
        level: MasteryLevel,
        date: date_type,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        self._level = level
        self._date = date

    @property
    def level(self) -> MasteryLevel:
        return self._level

    @property
    def date(self) -> date_type:
        return self._date
