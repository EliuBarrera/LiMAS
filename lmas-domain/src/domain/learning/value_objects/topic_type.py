"""Tipo de un LearningTopic."""
from enum import Enum


class TopicType(str, Enum):
    PROGRAMMING = "programming"
    DATABASE = "database"
    TOOL = "tool"
    SOFT_SKILL = "soft_skill"
    INTERVIEW = "interview"
