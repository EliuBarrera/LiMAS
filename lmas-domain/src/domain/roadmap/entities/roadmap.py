"""
Roadmap: raíz de agregado que representa una ruta de aprendizaje completa
(ej: Backend Python, Inteligencia Artificial, DevOps).

Contiene sus Phase y sus WeeklyReview. Toda modificación a estas entidades
hijas debe pasar por métodos del Roadmap, para mantener las invariantes
del agregado.
"""
from datetime import date
from uuid import UUID

from domain.shared.entity import AggregateRoot
from domain.shared.exceptions import BusinessRuleViolationError, InvalidValueError
from domain.roadmap.entities.phase import Phase
from domain.roadmap.entities.weekly_review import WeeklyReview
from domain.roadmap.value_objects.roadmap_status import RoadmapStatus


class Roadmap(AggregateRoot):
    def __init__(
        self,
        user_id: UUID,
        name: str,
        description: str = "",
        start_date: date | None = None,
        end_date: date | None = None,
        status: RoadmapStatus = RoadmapStatus.PLANNED,
        phases: list[Phase] | None = None,
        weekly_reviews: list[WeeklyReview] | None = None,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not name or not name.strip():
            raise InvalidValueError("El nombre del roadmap no puede estar vacío.")
        if start_date and end_date and end_date < start_date:
            raise InvalidValueError("La fecha de fin no puede ser anterior a la fecha de inicio.")

        self._user_id = user_id
        self._name = name.strip()
        self._description = description
        self._start_date = start_date
        self._end_date = end_date
        self._status = status
        self._phases: list[Phase] = phases or []
        self._weekly_reviews: list[WeeklyReview] = weekly_reviews or []

    # --- getters ---
    @property
    def user_id(self) -> UUID:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def status(self) -> RoadmapStatus:
        return self._status

    @property
    def phases(self) -> list[Phase]:
        return sorted(self._phases, key=lambda p: p.order)

    @property
    def weekly_reviews(self) -> list[WeeklyReview]:
        return list(self._weekly_reviews)

    # --- comportamiento ---
    def add_phase(self, name: str, description: str = "") -> Phase:
        if self._status == RoadmapStatus.ARCHIVED:
            raise BusinessRuleViolationError("No se pueden agregar fases a un roadmap archivado.")
        next_order = len(self._phases)
        phase = Phase(name=name, description=description, order=next_order)
        self._phases.append(phase)
        return phase

    def add_weekly_review(self, review: WeeklyReview) -> None:
        self._weekly_reviews.append(review)

    def start(self) -> None:
        if not self._phases:
            raise BusinessRuleViolationError("Un roadmap necesita al menos una fase para poder iniciarse.")
        self._status = RoadmapStatus.IN_PROGRESS

    def pause(self) -> None:
        if self._status != RoadmapStatus.IN_PROGRESS:
            raise BusinessRuleViolationError("Solo un roadmap en progreso puede pausarse.")
        self._status = RoadmapStatus.PAUSED

    def complete(self) -> None:
        if self._status not in (RoadmapStatus.IN_PROGRESS, RoadmapStatus.PAUSED):
            raise BusinessRuleViolationError("Solo un roadmap en progreso o pausado puede completarse.")
        self._status = RoadmapStatus.COMPLETED

    def archive(self) -> None:
        self._status = RoadmapStatus.ARCHIVED
