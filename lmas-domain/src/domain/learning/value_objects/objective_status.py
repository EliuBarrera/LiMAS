"""Estado de un LearningObjective."""
from enum import Enum


class ObjectiveStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
