# Learning Management & Analytics System (LiMAS)

## Objetivo

Construir un sistema que permita gestionar y analizar el proceso de aprendizaje de forma integral, no solo registrar horas de estudio.

El sistema debe responder preguntas como:

- ¿Cuántas horas he dedicado a un tema?
- ¿Qué tan rápido estoy resolviendo ejercicios?
- ¿Qué temas domino y cuáles debo reforzar?
- ¿Qué recursos me ayudan más?
- ¿Cuál ha sido mi progreso en los últimos meses?

---

# Modelo del dominio

```
Usuario
    │
    └── Roadmaps
            │
            ├── Fases
            │       │
            │       └── Temas
            │               │
            │               ├── Objetivos
            │               ├── Registros de estudio
            │               ├── Evaluaciones
            │               ├── Intentos de ejercicios
            │               └── Recursos
            │
            └── Revisiones semanales

Usuario
    ├── Proyectos
    │       └── Funcionalidades
    │
    └── Logros
```

---

# Entidades

## User

Representa al estudiante.

### Atributos

- id
- nombre
- email
- fechaRegistro

### Relaciones

- 1 → N Roadmap
- 1 → N Project
- 1 → N Achievement

---

## Roadmap

Representa una ruta de aprendizaje.

Ejemplos:

- Backend Python
- Inteligencia Artificial
- DevOps

### Atributos

- id
- nombre
- descripción
- fechaInicio
- fechaFin
- estado

### Relaciones

- 1 → N Phase
- 1 → N WeeklyReview

---

## Phase

Agrupa un conjunto de temas.

Ejemplo:

- Lógica
- Estructuras de Datos
- Algoritmos

### Atributos

- id
- nombre
- descripción
- orden

### Relaciones

- 1 → N LearningTopic

---

## LearningTopic

Unidad principal del aprendizaje.

Ejemplos:

- Arrays
- HashMap
- JWT
- Docker
- SQL JOIN

### Atributos

- id
- nombre
- descripción
- tipo

Tipos posibles:

- Programming
- Database
- Tool
- SoftSkill
- Interview

### Relaciones

- 1 → N LearningObjective
- 1 → N StudyRecord
- 1 → N KnowledgeAssessment
- 1 → N ExerciseAttempt
- N → N Resource

---

## LearningObjective

Objetivos específicos de un tema.

Ejemplos:

- Resolver 20 ejercicios
- Comprender complejidad temporal
- Explicar cuándo usar HashMap

### Atributos

- id
- título
- descripción
- prioridad
- estado

---

## StudyRecord

Registro de estudio sobre un tema en una fecha determinada.

Ejemplo:

Hoy:

- Arrays (45 min)
- SQL (30 min)
- Docker (20 min)

Se generan tres StudyRecord.

### Atributos

- id
- fecha
- duración
- energía
- concentración
- notas

---

## Resource

Material utilizado durante el estudio.

Ejemplos:

- Libro
- Video
- Curso
- Artículo
- Documentación
- Blog

### Atributos

- id
- nombre
- tipo
- url

---

## Exercise

Ejercicio de programación.

Ejemplos:

- Two Sum
- Valid Parentheses

### Atributos

- id
- plataforma
- título
- dificultad
- url

---

## ExerciseAttempt

Representa cada intento realizado sobre un ejercicio.

### Atributos

- id
- tiempo
- resultado
- intentos
- usoPistas
- usoIA
- explicaciónPropia
- complejidad

Permite medir:

- tiempo promedio
- tasa de éxito
- dependencia de IA
- mejora a lo largo del tiempo

---

## KnowledgeAssessment

Nivel de dominio de un tema.

Escala:

- 0 → No entiendo
- 1 → Lo entiendo
- 2 → Lo resuelvo
- 3 → Lo puedo enseñar

### Atributos

- id
- nivel
- fecha

---

## WeeklyReview

Resumen semanal.

### Atributos

- id
- semana
- fortalezas
- debilidades
- acciones

---

## Project

Proyecto práctico.

Ejemplos:

- Sistema Hospitalario
- API REST
- Tracker de aprendizaje

### Atributos

- id
- nombre
- descripción
- github
- estado

### Relaciones

- 1 → N ProjectFeature

---

## ProjectFeature

Funcionalidades del proyecto.

Ejemplos:

- JWT
- Docker
- Swagger
- Redis
- CI/CD

### Atributos

- id
- nombre
- estado
- fechaCompletado

---

## Achievement

Sistema de logros.

Ejemplos:

- 100 ejercicios resueltos
- 30 días consecutivos
- Primer proyecto terminado
- Primer problema Hard
- Primera entrevista técnica

### Atributos

- id
- nombre
- descripción
- fecha

---

# Relaciones principales

```
User
│
├── Roadmap
│      │
│      ├── Phase
│      │      │
│      │      └── LearningTopic
│      │               │
│      │               ├── LearningObjective
│      │               ├── StudyRecord
│      │               ├── ExerciseAttempt
│      │               ├── KnowledgeAssessment
│      │               └── Resource
│      │
│      └── WeeklyReview
│
├── Project
│      └── ProjectFeature
│
└── Achievement
```

---

# Principio de diseño

El centro del modelo es **LearningTopic**, no la sesión de estudio.

La sesión representa tiempo invertido.

El tema representa conocimiento adquirido.

Toda la información (ejercicios, evaluaciones, recursos y registros de estudio) gira alrededor del tema para facilitar el análisis del aprendizaje y la generación de métricas.

---

# Objetivo final

Construir un sistema capaz de responder preguntas como:

- ¿Cuántas horas he estudiado Arrays?
- ¿Qué recursos fueron más efectivos para aprender Docker?
- ¿Cuál es mi progreso en SQL?
- ¿Qué temas no practico desde hace semanas?
- ¿Cuánto ha mejorado mi tiempo resolviendo ejercicios?
- ¿Cuál es mi nivel de dominio por cada tema del roadmap?
