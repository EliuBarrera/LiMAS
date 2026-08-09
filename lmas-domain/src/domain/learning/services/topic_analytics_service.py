"""
Servicio de dominio: lógica que compara/agrega varios LearningTopic.

Un domain service se usa (en vez de un método de la entidad) cuando la
operación involucra a MÁS DE UN agregado y no pertenece naturalmente a
ninguno de ellos en particular.
"""
from datetime import date as date_type

from domain.learning.entities.learning_topic import LearningTopic


class TopicAnalyticsService:
    @staticmethod
    def stale_topics(topics: list[LearningTopic], reference_date: date_type, threshold_days: int = 14) -> list[LearningTopic]:
        """¿Qué temas no practico desde hace semanas?"""
        stale = []
        for topic in topics:
            days = topic.days_since_last_study(reference_date)
            if days is None or days >= threshold_days:
                stale.append(topic)
        return stale

    @staticmethod
    def weakest_topics(topics: list[LearningTopic], limit: int = 5) -> list[LearningTopic]:
        """¿Qué temas domino y cuáles debo reforzar? Ordena por nivel de dominio ascendente."""
        assessed = [t for t in topics if t.current_mastery_level() is not None]
        assessed.sort(key=lambda t: t.current_mastery_level())
        return assessed[:limit]

    @staticmethod
    def total_hours_by_topic(topics: list[LearningTopic]) -> dict[str, float]:
        """¿Cuántas horas he dedicado a cada tema?"""
        result: dict[str, float] = {}
        for topic in topics:
            total = topic.total_study_time()
            result[topic.name] = round(total.minutes / 60, 2) if total else 0.0
        return result
