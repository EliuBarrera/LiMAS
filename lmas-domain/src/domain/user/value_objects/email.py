"""Value Object Email: garantiza que un correo siempre sea válido dentro del dominio."""
import re
from dataclasses import dataclass

from domain.shared.exceptions import InvalidValueError

_EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self) -> None:
        if not self.value or not _EMAIL_PATTERN.match(self.value):
            raise InvalidValueError(f"Email inválido: '{self.value}'")
        # Normalizamos a minúsculas para evitar duplicados por casing.
        object.__setattr__(self, "value", self.value.strip().lower())

    def __str__(self) -> str:
        return self.value
