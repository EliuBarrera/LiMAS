# LMAS — Domain Layer (Clean Architecture + DDD)

## Estructura por Bounded Context

```
src/domain/
├── shared/                      # Entity, AggregateRoot, ValueObject, excepciones de dominio
├── user/                        # Aggregate: User
├── roadmap/                     # Aggregate: Roadmap (contiene Phase, WeeklyReview)
├── learning/                    # Aggregate: LearningTopic (centro del modelo)
│   ├── entities/                #   contiene LearningObjective, StudyRecord,
│   │                             #   ExerciseAttempt, KnowledgeAssessment
│   └── services/                #   TopicAnalyticsService (domain service multi-agregado)
├── resource/                    # Aggregate: Resource
├── exercise/                    # Aggregate: Exercise
├── project/                     # Aggregate: Project (contiene ProjectFeature)
└── achievement/                 # Aggregate: Achievement
```

## Reglas de diseño aplicadas

1. **Agregados pequeños**: cada carpeta de primer nivel = un Aggregate Root con su propio
   repositorio. Las relaciones ENTRE agregados (Phase -> LearningTopic, LearningTopic ->
   Resource/Exercise) se guardan como **UUID**, nunca como objeto anidado.
2. **Cero dependencias de framework**: no hay imports de FastAPI, SQLAlchemy, Pydantic
   ni nada externo — solo `dataclasses`, `enum`, `abc`, `uuid`, `datetime` (stdlib).
3. **Invariantes protegidas en el constructor / métodos**, no en la capa externa
   (ej: `Duration` no permite <= 0, `Email` valida formato, `Roadmap.start()` exige fases).
4. **Repositorios como interfaces (`ABC`)**: la implementación con SQLAlchemy se
   hará después, en `infrastructure/repositories/`, sin que el dominio se entere.
5. **Domain Service** (`TopicAnalyticsService`) solo para lógica que cruza varios
   `LearningTopic` a la vez (temas atrasados, temas más débiles) — no pertenece a
   ninguna instancia individual.

## Próximo paso (según el flujo progresivo)

DOMAIN ✅ → **Application** (Use Cases que orquestan estos agregados) → Infrastructure
(SQLAlchemy/Alembic implementando los repositorios) → Presentation (FastAPI).
