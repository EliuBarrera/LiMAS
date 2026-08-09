"""Estado de un Roadmap."""
from enum import Enum


class RoadmapStatus(str, Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    COMPLETED = "completed"
    ARCHIVED = "archived"
