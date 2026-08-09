# Revisión del Dominio (Clean Architecture + DDD)

## Evaluación general

La organización actual del dominio es muy buena y sigue correctamente los principios de **Clean Architecture** y una aproximación inicial a **Domain-Driven Design (DDD)**.

### Calificación

| Aspecto | Nota |
|----------|------|
| Organización | 10/10 |
| Separación por dominio | 10/10 |
| Uso de Value Objects | 9.5/10 |
| Repositorios | 10/10 |
| Escalabilidad | 9.5/10 |
| Aplicación de DDD | 8.5/10 |

**Calificación general: 9.5/10**

---

# Correcciones propuestas

## 1. Reemplazar el módulo `exercise` por `practice`

Actualmente:

```text
exercise/
    entities/
        exercise.py

learning/
    entities/
        exercise_attempt.py
```

### Problema

`Exercise` y `ExerciseAttempt` pertenecen al mismo contexto de negocio.

Un intento de ejercicio no forma parte del aprendizaje en sí, sino del proceso de práctica.

### Propuesta

```text
practice/

    entities/
        exercise.py
        exercise_attempt.py

    repositories/
        practice_repository.py

    value_objects/
        difficulty.py
        attempt_result.py
```

De esta manera ambos conceptos quedan agrupados dentro del mismo Bounded Context.

---

## 2. Mover `Resource` al dominio `learning`

Actualmente:

```text
resource/
```

### Problema

Un recurso nunca existe por sí solo.

Siempre está asociado al aprendizaje de un tema.

Ejemplo:

```
LearningTopic

↓

Resources
```

### Propuesta

```text
learning/

    entities/

        learning_topic.py

        resource.py
```

El módulo `resource` deja de existir como dominio independiente.

---

## 3. Mover `WeeklyReview` al dominio `learning`

Actualmente:

```text
roadmap/
    weekly_review.py
```

### Problema

Una revisión semanal evalúa el aprendizaje, no el roadmap.

Preguntas que responde:

- ¿Qué aprendí esta semana?
- ¿Qué dificultades tuve?
- ¿Qué debo mejorar?

No responde al estado del roadmap.

### Propuesta

```text
learning/

    entities/

        weekly_review.py
```

---

## 4. Revisar `TopicAnalyticsService`

Actualmente:

```text
learning/
    services/
        topic_analytics_service.py
```

### Verificar su responsabilidad

Debe permanecer en el dominio **únicamente si**:

- Calcula progreso.
- Calcula dominio del tema.
- Valida reglas del negocio.

Debe moverse a la capa **Application** si:

- Construye dashboards.
- Genera reportes.
- Consulta múltiples repositorios.
- Calcula estadísticas para mostrar al usuario.

Regla general:

- **Domain Service → lógica de negocio.**
- **Application Service → orquestación y consultas.**

---

## 5. Preparar carpeta para Domain Events

No es necesario implementarlos todavía.

Sin embargo, es recomendable reservar la estructura.

```text
learning/

    events/

        TopicCompleted.py

        StudyRecordCreated.py

achievement/

    events/

        AchievementUnlocked.py
```

Los eventos aparecerán únicamente cuando el dominio realmente los necesite.

---

## 6. Agregar Factories

Cuando una entidad requiera una construcción compleja, utilizar una Factory.

Evitar:

```python
Roadmap(...)
```

Con una gran cantidad de parámetros.

Preferir:

```python
RoadmapFactory.create(...)
```

Posible estructura:

```text
roadmap/

    factories/

        roadmap_factory.py
```

---

## 7. Definir Aggregate Roots

No todas las entidades deben poder modificarse directamente.

### Roadmap

```
Roadmap

↓

Phase

↓

LearningTopic

↓

LearningObjective
```

El Aggregate Root debe ser:

```
Roadmap
```

Las operaciones sobre `Phase` deberían realizarse únicamente mediante el Roadmap.

Ejemplo:

```
Roadmap.add_phase()

Roadmap.remove_phase()
```

---

### Project

```
Project

↓

ProjectFeature
```

Aggregate Root:

```
Project
```

Las funcionalidades deben administrarse únicamente desde el proyecto.

---

## 8. Crear Value Objects compartidos

Actualmente existen Value Objects específicos para cada módulo.

También es recomendable crear objetos reutilizables.

Propuesta:

```text
shared/

    value_objects/

        Identifier.py

        Name.py

        Description.py

        Url.py

        Timestamp.py
```

Estos podrán reutilizarse en múltiples dominios.

---

## 9. Agregar el dominio `analytics`

Actualmente las métricas parecen pertenecer a `learning`.

Sin embargo, conceptualmente forman otro contexto.

Ejemplos:

- Horas estudiadas.
- Tiempo promedio por ejercicio.
- Dominio por tema.
- Progreso mensual.
- Streaks.
- Dashboard.

### Propuesta

```text
analytics/

    entities/

    services/

    repositories/
```

Este dominio será responsable únicamente de analizar información, nunca de modificar el aprendizaje.

---

# Estructura propuesta

```text
domain/

├── shared/
├── user/
├── roadmap/
├── learning/
├── practice/
├── project/
├── analytics/
└── achievement/
```

El dominio `exercise` desaparece y es absorbido por `practice`.

---

# Recomendaciones finales

- No crear carpetas "por si acaso".
- Incorporar `events`, `factories` o `specifications` únicamente cuando el dominio realmente los requiera.
- Mantener el dominio completamente independiente de cualquier framework.
- Continuar con el diseño de las entidades y sus reglas de negocio antes de comenzar la capa **Application**.
- No implementar aún SQLAlchemy, FastAPI o PostgreSQL; primero consolidar el modelo del dominio.

---

# Próximo paso recomendado

Antes de construir la infraestructura, definir completamente:

- Entidades.
- Agregados (Aggregate Roots).
- Invariantes del dominio.
- Métodos de negocio.
- Relaciones entre entidades.

Una vez el dominio sea sólido, se podrá desarrollar la capa **Application**, seguida de **Infrastructure** y finalmente **Presentation**.
