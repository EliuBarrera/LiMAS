"""
Clase base para Value Objects (objetos de valor).

Un Value Object no tiene identidad: dos instancias con los mismos
atributos son iguales entre sí. Son inmutables por diseño (frozen dataclass).
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject:
    """Marcador base para value objects inmutables."""
    pass
