"""ProjectFeature: funcionalidad concreta de un Project (ej: JWT, Docker, Swagger, Redis, CI/CD)."""
from datetime import date as date_type
from uuid import UUID

from domain.shared.entity import Entity
from domain.shared.exceptions import InvalidValueError
from domain.project.value_objects.feature_status import FeatureStatus


class ProjectFeature(Entity):
    def __init__(
        self,
        name: str,
        status: FeatureStatus = FeatureStatus.PENDING,
        completed_date: date_type | None = None,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not name or not name.strip():
            raise InvalidValueError("El nombre de la funcionalidad no puede estar vacío.")
        self._name = name.strip()
        self._status = status
        self._completed_date = completed_date

    @property
    def name(self) -> str:
        return self._name

    @property
    def status(self) -> FeatureStatus:
        return self._status

    @property
    def completed_date(self) -> date_type | None:
        return self._completed_date

    def complete(self, completed_date: date_type) -> None:
        self._status = FeatureStatus.DONE
        self._completed_date = completed_date
