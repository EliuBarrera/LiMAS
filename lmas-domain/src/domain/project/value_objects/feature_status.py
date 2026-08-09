"""Estado de una ProjectFeature."""
from enum import Enum


class FeatureStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"
