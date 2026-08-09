"""Project: raíz de agregado de un proyecto práctico (ej: API REST, Tracker de aprendizaje)."""
from uuid import UUID

from domain.shared.entity import AggregateRoot
from domain.shared.exceptions import BusinessRuleViolationError, InvalidValueError
from domain.project.entities.project_feature import ProjectFeature
from domain.project.value_objects.project_status import ProjectStatus


class Project(AggregateRoot):
    def __init__(
        self,
        user_id: UUID,
        name: str,
        description: str = "",
        github: str = "",
        status: ProjectStatus = ProjectStatus.PLANNED,
        features: list[ProjectFeature] | None = None,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not name or not name.strip():
            raise InvalidValueError("El nombre del proyecto no puede estar vacío.")
        self._user_id = user_id
        self._name = name.strip()
        self._description = description
        self._github = github
        self._status = status
        self._features: list[ProjectFeature] = features or []

    @property
    def user_id(self) -> UUID:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def status(self) -> ProjectStatus:
        return self._status

    @property
    def features(self) -> list[ProjectFeature]:
        return list(self._features)

    def add_feature(self, name: str) -> ProjectFeature:
        feature = ProjectFeature(name=name)
        self._features.append(feature)
        return feature

    def complete_feature(self, feature_id: UUID, completed_date) -> None:
        feature = next((f for f in self._features if f.id == feature_id), None)
        if feature is None:
            raise BusinessRuleViolationError("La funcionalidad no pertenece a este proyecto.")
        feature.complete(completed_date)

    def completion_percentage(self) -> float:
        """Porcentaje de funcionalidades completadas del proyecto."""
        from domain.project.value_objects.feature_status import FeatureStatus
        if not self._features:
            return 0.0
        done = sum(1 for f in self._features if f.status == FeatureStatus.DONE)
        return round(done / len(self._features) * 100, 2)

    def start(self) -> None:
        self._status = ProjectStatus.IN_PROGRESS

    def complete(self) -> None:
        self._status = ProjectStatus.COMPLETED

    def abandon(self) -> None:
        self._status = ProjectStatus.ABANDONED
