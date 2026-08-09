"""
LearningTopic: raíz de agregado y CENTRO del modelo de dominio (ver
"Principio de diseño" en la documentación del proyecto).

La sesión de estudio representa tiempo invertido; el tema representa
conocimiento adquirido. Todo (objetivos, registros de estudio, intentos
de ejercicios, evaluaciones y recursos) gira alrededor de LearningTopic
para poder calcular métricas de aprendizaje.
"""
from datetime import date as date_type
from uuid import UUID

from domain.shared.entity import AggregateRoot
from domain.shared.exceptions import InvalidValueError
from domain.learning.value_objects.topic_type import TopicType
from domain.learning.value_objects.duration import Duration
from domain.learning.value_objects.mastery_level import MasteryLevel
from domain.learning.entities.learning_objective import LearningObjective
from domain.learning.entities.study_record import StudyRecord
from domain.learning.entities.exercise_attempt import ExerciseAttempt
from domain.learning.entities.knowledge_assessment import KnowledgeAssessment


class LearningTopic(AggregateRoot):
    def __init__(
        self,
        phase_id: UUID,
        name: str,
        description: str = "",
        topic_type: TopicType = TopicType.PROGRAMMING,
        objectives: list[LearningObjective] | None = None,
        study_records: list[StudyRecord] | None = None,
        exercise_attempts: list[ExerciseAttempt] | None = None,
        knowledge_assessments: list[KnowledgeAssessment] | None = None,
        resource_ids: list[UUID] | None = None,
        id: UUID | None = None,
    ) -> None:
        super().__init__(id)
        if not name or not name.strip():
            raise InvalidValueError("El nombre del tema no puede estar vacío.")

        self._phase_id = phase_id
        self._name = name.strip()
        self._description = description
        self._topic_type = topic_type
        self._objectives: list[LearningObjective] = objectives or []
        self._study_records: list[StudyRecord] = study_records or []
        self._exercise_attempts: list[ExerciseAttempt] = exercise_attempts or []
        self._knowledge_assessments: list[KnowledgeAssessment] = knowledge_assessments or []
        self._resource_ids: list[UUID] = resource_ids or []

    # --- getters ---
    @property
    def phase_id(self) -> UUID:
        return self._phase_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def topic_type(self) -> TopicType:
        return self._topic_type

    @property
    def objectives(self) -> list[LearningObjective]:
        return list(self._objectives)

    @property
    def study_records(self) -> list[StudyRecord]:
        return list(self._study_records)

    @property
    def exercise_attempts(self) -> list[ExerciseAttempt]:
        return list(self._exercise_attempts)

    @property
    def knowledge_assessments(self) -> list[KnowledgeAssessment]:
        return list(self._knowledge_assessments)

    @property
    def resource_ids(self) -> list[UUID]:
        return list(self._resource_ids)

    # --- comportamiento: construcción del agregado ---
    def add_objective(self, title: str, description: str = "", priority=None) -> LearningObjective:
        from domain.learning.value_objects.priority import Priority
        objective = LearningObjective(
            title=title,
            description=description,
            priority=priority or Priority.MEDIUM,
        )
        self._objectives.append(objective)
        return objective

    def log_study_session(
        self,
        date: date_type,
        duration: Duration,
        energy: int | None = None,
        concentration: int | None = None,
        notes: str = "",
    ) -> StudyRecord:
        """Registra una sesión de estudio. Un mismo día puede tener varios registros."""
        record = StudyRecord(
            date=date, duration=duration, energy=energy,
            concentration=concentration, notes=notes,
        )
        self._study_records.append(record)
        return record

    def record_exercise_attempt(
        self,
        exercise_id: UUID,
        time_spent: Duration,
        result,
        attempts_count: int = 1,
        used_hints: bool = False,
        used_ai: bool = False,
        self_explanation: str = "",
        complexity_analysis: str = "",
    ) -> ExerciseAttempt:
        attempt = ExerciseAttempt(
            exercise_id=exercise_id,
            time_spent=time_spent,
            result=result,
            attempts_count=attempts_count,
            used_hints=used_hints,
            used_ai=used_ai,
            self_explanation=self_explanation,
            complexity_analysis=complexity_analysis,
        )
        self._exercise_attempts.append(attempt)
        return attempt

    def assess_knowledge(self, level: MasteryLevel, date: date_type) -> KnowledgeAssessment:
        assessment = KnowledgeAssessment(level=level, date=date)
        self._knowledge_assessments.append(assessment)
        return assessment

    def link_resource(self, resource_id: UUID) -> None:
        if resource_id not in self._resource_ids:
            self._resource_ids.append(resource_id)

    def unlink_resource(self, resource_id: UUID) -> None:
        if resource_id in self._resource_ids:
            self._resource_ids.remove(resource_id)

    # --- comportamiento: métricas / analítica (responde las preguntas del objetivo del sistema) ---
    def total_study_time(self) -> Duration | None:
        """¿Cuántas horas he dedicado a este tema? None si aún no hay registros."""
        if not self._study_records:
            return None
        total_minutes = sum(r.duration.minutes for r in self._study_records)
        return Duration(minutes=total_minutes)

    def average_exercise_time(self) -> Duration | None:
        """¿Qué tan rápido estoy resolviendo ejercicios, en promedio?"""
        if not self._exercise_attempts:
            return None
        total = sum(a.time_spent.minutes for a in self._exercise_attempts)
        return Duration(minutes=round(total / len(self._exercise_attempts)))

    def success_rate(self) -> float | None:
        """Porcentaje de intentos de ejercicio exitosos."""
        from domain.learning.value_objects.attempt_result import AttemptResult
        if not self._exercise_attempts:
            return None
        successes = sum(1 for a in self._exercise_attempts if a.result == AttemptResult.SUCCESS)
        return round(successes / len(self._exercise_attempts) * 100, 2)

    def ai_dependency_rate(self) -> float | None:
        """¿Qué tan dependiente he sido de la IA para resolver ejercicios de este tema?"""
        if not self._exercise_attempts:
            return None
        ai_assisted = sum(1 for a in self._exercise_attempts if a.used_ai)
        return round(ai_assisted / len(self._exercise_attempts) * 100, 2)

    def current_mastery_level(self) -> MasteryLevel | None:
        """¿Qué tan bien domino este tema? Se basa en la evaluación más reciente."""
        if not self._knowledge_assessments:
            return None
        latest = max(self._knowledge_assessments, key=lambda a: a.date)
        return latest.level

    def days_since_last_study(self, reference_date: date_type) -> int | None:
        """¿Qué temas no practico desde hace semanas?"""
        if not self._study_records:
            return None
        last_date = max(r.date for r in self._study_records)
        return (reference_date - last_date).days
