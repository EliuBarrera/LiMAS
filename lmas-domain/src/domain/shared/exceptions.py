"""Excepciones del dominio. No dependen de ningún framework."""


class DomainError(Exception):
    """Excepción base para toda violación de una regla de negocio."""


class InvalidValueError(DomainError):
    """Un value object o atributo recibió un valor inválido."""


class BusinessRuleViolationError(DomainError):
    """Se intentó ejecutar una operación que viola una regla de negocio."""


class EntityNotFoundError(DomainError):
    """Se buscó una entidad que no existe (usado por implementaciones de repositorio)."""
