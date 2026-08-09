"""WeeklyReview: resumen semanal de fortalezas, debilidades y acciones dentro de un Roadmap."""
from uuid import UUID

from domain.shared.entity import Entity
from domain.shared.exceptions import InvalidValueError


class WeeklyReview(Entity):
    def __init__(
        self,
        week: str,
        strengths: list[str] | None = None,
        weaknesses: list[str] | None = None,
        actions: list[str] | None = None,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not week or not week.strip():
            raise InvalidValueError("La semana de la revisión no puede estar vacía.")
        self._week = week.strip()
        self._strengths = strengths or []
        self._weaknesses = weaknesses or []
        self._actions = actions or []

    @property
    def week(self) -> str:
        return self._week

    @property
    def strengths(self) -> list[str]:
        return list(self._strengths)

    @property
    def weaknesses(self) -> list[str]:
        return list(self._weaknesses)

    @property
    def actions(self) -> list[str]:
        return list(self._actions)

    def add_strength(self, text: str) -> None:
        self._strengths.append(text)

    def add_weakness(self, text: str) -> None:
        self._weaknesses.append(text)

    def add_action(self, text: str) -> None:
        self._actions.append(text)
