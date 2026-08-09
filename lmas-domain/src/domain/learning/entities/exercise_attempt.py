"""
ExerciseAttempt: cada intento realizado sobre un Exercise, dentro del
contexto de un LearningTopic. Permite medir tiempo, tasa de éxito y
dependencia de IA/pistas a lo largo del tiempo.
"""
from uuid import UUID

from domain.shared.entity import Entity
from domain.shared.exceptions import InvalidValueError
from domain.learning.value_objects.duration import Duration
from domain.learning.value_objects.attempt_result import AttemptResult


class ExerciseAttempt(Entity):
    def __init__(
        self,
        exercise_id: UUID,
        time_spent: Duration,
        result: AttemptResult,
        attempts_count: int = 1,
        used_hints: bool = False,
        used_ai: bool = False,
        self_explanation: str = "",
        complexity_analysis: str = "",
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if attempts_count < 1:
            raise InvalidValueError("El número de intentos debe ser al menos 1.")
        self._exercise_id = exercise_id
        self._time_spent = time_spent
        self._result = result
        self._attempts_count = attempts_count
        self._used_hints = used_hints
        self._used_ai = used_ai
        self._self_explanation = self_explanation
        self._complexity_analysis = complexity_analysis

    @property
    def exercise_id(self) -> UUID:
        return self._exercise_id

    @property
    def time_spent(self) -> Duration:
        return self._time_spent

    @property
    def result(self) -> AttemptResult:
        return self._result

    @property
    def attempts_count(self) -> int:
        return self._attempts_count

    @property
    def used_hints(self) -> bool:
        return self._used_hints

    @property
    def used_ai(self) -> bool:
        return self._used_ai

    @property
    def was_independent(self) -> bool:
        """Regla de negocio: un intento se considera independiente si no usó pistas ni IA."""
        return not self._used_hints and not self._used_ai
