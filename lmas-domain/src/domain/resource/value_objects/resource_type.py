"""Tipo de material de estudio."""
from enum import Enum


class ResourceType(str, Enum):
    BOOK = "book"
    VIDEO = "video"
    COURSE = "course"
    ARTICLE = "article"
    DOCUMENTATION = "documentation"
    BLOG = "blog"
