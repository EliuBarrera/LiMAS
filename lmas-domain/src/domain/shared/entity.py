"""
Clase base para todas las entidades del dominio.

Una Entity se distingue por su identidad (id), no por sus atributos.
Dos entidades con los mismos atributos pero distinto id son objetos distintos.
"""
from abc import ABC
from uuid import UUID, uuid4


class Entity(ABC):
    """Entidad base con identidad propia."""

    def __init__(self, id: UUID | None = None) -> None:
        self._id: UUID = id or uuid4()

    @property
    def id(self) -> UUID:
        return self._id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        return self.__class__ is other.__class__ and self._id == other._id

    def __hash__(self) -> int:
        return hash((self.__class__, self._id))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self._id})"


class AggregateRoot(Entity):
    """
    Marca las entidades que son raíz de un agregado.

    Solo se debe acceder al agregado a través de su raíz (por ejemplo,
    LearningTopic es la raíz; sus StudyRecord/ExerciseAttempt/etc. no
    deben ser accedidos ni modificados directamente desde fuera).
    Los repositorios solo existen para AggregateRoots.
    """
    pass
