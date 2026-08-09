"""
Escala de dominio de un tema (KnowledgeAssessment).

0 -> No entiendo
1 -> Lo entiendo
2 -> Lo resuelvo
3 -> Lo puedo enseñar
"""
from enum import IntEnum


class MasteryLevel(IntEnum):
    NOT_UNDERSTOOD = 0
    UNDERSTAND = 1
    CAN_SOLVE = 2
    CAN_TEACH = 3
