"""Resultado de un ExerciseAttempt."""
from enum import Enum


class AttemptResult(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    PARTIAL = "partial"
