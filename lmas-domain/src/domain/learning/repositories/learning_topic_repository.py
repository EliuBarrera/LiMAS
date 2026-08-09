"""Interfaz del repositorio de LearningTopic."""
from abc import ABC, abstractmethod
from uuid import UUID

from domain.learning.entities.learning_topic import LearningTopic


class LearningTopicRepository(ABC):
    @abstractmethod
    def save(self, topic: LearningTopic) -> None: ...

    @abstractmethod
    def get_by_id(self, topic_id: UUID) -> LearningTopic | None: ...

    @abstractmethod
    def list_by_phase(self, phase_id: UUID) -> list[LearningTopic]: ...

    @abstractmethod
    def list_by_resource(self, resource_id: UUID) -> list[LearningTopic]:
        """Necesario para responder: '¿qué recursos me ayudan más?' cruzando temas y recursos."""
        ...

    @abstractmethod
    def delete(self, topic_id: UUID) -> None: ...
