# Introducción a Clean Architecture

## ¿Qué es?

Clean Architecture es una arquitectura de software cuyo objetivo principal es **separar las reglas del negocio de los detalles técnicos**.

Su principio más importante es:

> **Las reglas del negocio no deben depender de frameworks, bases de datos o tecnologías externas.**

En otras palabras:

- El dominio debe funcionar aunque cambie FastAPI por Flask.
- El dominio debe funcionar aunque PostgreSQL sea reemplazado por MongoDB.
- El dominio debe funcionar aunque la interfaz deje de ser una API REST.

---

# El problema que resuelve

En una arquitectura tradicional es común encontrar código como este:

```python
@app.post("/topics")
def create_topic(topic):

    db = Session()

    db.add(topic)

    db.commit()
```

Aquí la lógica de negocio está completamente acoplada a:

- FastAPI
- SQLAlchemy
- PostgreSQL

Si alguna tecnología cambia, gran parte del código deberá modificarse.

Clean Architecture evita este problema.

---

# Principio fundamental

Las reglas del negocio son independientes de la tecnología.

Ejemplos de reglas del negocio:

- Un Roadmap contiene varias fases.
- Una fase contiene varios temas.
- Un StudyRecord debe tener una duración válida.
- Un ExerciseAttempt pertenece a un ejercicio.

Estas reglas existirían aunque el sistema estuviera escrito en cualquier otro lenguaje.

---

# Capas de Clean Architecture

```
+---------------------------+
|      Presentation         |
+---------------------------+
|      Application          |
+---------------------------+
|         Domain            |
+---------------------------+
|     Infrastructure        |
+---------------------------+
```

Aunque visualmente las capas parecen ir de arriba hacia abajo, las dependencias siempre apuntan hacia el dominio.

```
Presentation
      │
      ▼
Application
      │
      ▼
   Domain
      ▲
      │
Infrastructure
```

El dominio nunca conoce las capas externas.

---

# 1. Domain

Es el corazón del sistema.

Aquí viven:

- Entidades
- Reglas de negocio
- Objetos de valor
- Servicios de dominio
- Interfaces de repositorio

El dominio **no conoce**:

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT
- Redis

Ejemplo de entidades:

- Roadmap
- Phase
- LearningTopic
- StudyRecord
- ExerciseAttempt

Ejemplo:

```python
class LearningTopic:

    def complete(self):
        ...
```

Nunca debería existir algo como:

```python
from sqlalchemy import Column
```

El dominio debe ser completamente independiente.

---

# 2. Application

Representa los casos de uso del sistema.

Aquí se implementan las acciones que un usuario puede realizar.

Ejemplos:

- Crear Roadmap
- Registrar estudio
- Completar objetivo
- Agregar proyecto
- Registrar intento de ejercicio

Cada acción es un **Use Case**.

Ejemplo:

```
CreateTopicUseCase

↓

Recibe datos

↓

Valida reglas

↓

Guarda información

↓

Retorna resultado
```

Los casos de uso no conocen la base de datos.

Solo conocen interfaces.

Ejemplo:

```python
class TopicRepository:

    def save(...):
        pass
```

---

# 3. Infrastructure

Contiene todos los detalles técnicos.

Aquí viven:

- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- JWT
- APIs externas

Aquí se implementan las interfaces definidas en el dominio.

Ejemplo:

```python
class SQLTopicRepository(TopicRepository):
```

Internamente utilizará SQLAlchemy para almacenar la información.

Si mañana PostgreSQL cambia por MongoDB, únicamente esta capa debe modificarse.

---

# 4. Presentation

Es la puerta de entrada al sistema.

Puede implementarse mediante:

- API REST
- GraphQL
- CLI
- WebSocket

En este proyecto utilizará FastAPI.

Su única responsabilidad es:

- Recibir solicitudes HTTP
- Convertir datos de entrada (DTOs)
- Ejecutar un caso de uso
- Retornar una respuesta

No debe contener lógica de negocio.

---

# Flujo completo de una petición

```
Cliente

↓

POST /topics

↓

Presentation

↓

CreateTopicUseCase

↓

TopicRepository (interfaz)

↓

SQLTopicRepository

↓

PostgreSQL

↓

Respuesta

↓

Cliente
```

---

# Inversión de Dependencias

Este es el principio más importante de Clean Architecture.

## Incorrecto

```
CreateTopicUseCase

↓

SQLAlchemy
```

El caso de uso depende directamente de una tecnología.

---

## Correcto

```
CreateTopicUseCase

↓

TopicRepository

↓

SQLTopicRepository

↓

PostgreSQL
```

Ahora el caso de uso solo conoce una interfaz.

La implementación concreta queda desacoplada.

---

# Organización del proyecto

```
src/

├── domain/
│   └── roadmap/
│       ├── entities/
│       ├── value_objects/
│       ├── repositories/
│       └── services/
│
├── application/
│   └── roadmap/
│       └── use_cases/
│
├── infrastructure/
│   ├── database/
│   ├── repositories/
│   └── migrations/
│
└── presentation/
    └── api/
```

---

# Analogía del restaurante

## Domain

Las recetas.

Representan el conocimiento del negocio.

No dependen de la cocina.

---

## Application

El chef.

Coordina la preparación de los platos.

Utiliza las recetas.

---

## Infrastructure

La cocina.

Incluye:

- Hornos
- Neveras
- Utensilios
- Ingredientes

Son herramientas para ejecutar el trabajo.

---

## Presentation

El mesero.

Recibe el pedido del cliente.

Lo entrega al chef.

Finalmente sirve el plato.

No cocina.

---

# Desarrollo del proyecto

El backend se desarrollará siguiendo este orden:

1. Diseñar el dominio.
2. Crear las entidades.
3. Definir reglas de negocio.
4. Diseñar interfaces de repositorio.
5. Implementar los casos de uso.
6. Implementar la infraestructura (SQLAlchemy, PostgreSQL, Alembic).
7. Exponer los casos de uso mediante FastAPI.

---

# Idea clave

En Clean Architecture:

- La base de datos es un detalle.
- El framework es un detalle.
- La API es un detalle.

El verdadero corazón del sistema es el **dominio**, donde viven las reglas de negocio y el modelo del problema que se desea resolver.
