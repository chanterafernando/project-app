# Thesis Management

Sistema web para gestionar el proceso de titulación: estudiantes, tesis, tutores, revisores, periodos académicos, verificación de plagio y defensas.

[![CI](https://github.com/USUARIO/thesis-management/actions/workflows/ci.yml/badge.svg)](https://github.com/USUARIO/thesis-management/actions/workflows/ci.yml)

> Reemplaza `USUARIO` por tu usuario u organización de GitHub para que se vea el estado del CI.

## Stack

| Capa | Tecnología |
|---|---|
| API | Python 3.13 · FastAPI |
| ORM y migraciones | SQLAlchemy 2.0 · Alembic |
| Base de datos | MySQL 8 (SQLite en pruebas) |
| Calidad | Ruff (lint) · pytest |
| CI | GitHub Actions |

## Estructura

```
thesis-management/
├── .github/workflows/ci.yml   Pipeline de CI (lint, pruebas, migraciones en MySQL)
├── backend/
│   ├── app/
│   │   ├── main.py            Aplicación FastAPI
│   │   ├── config.py          Lectura de variables de entorno
│   │   ├── database.py        Engine, sesión y Base de SQLAlchemy
│   │   ├── models/            Esquema base (§3.1 del documento de punto de partida)
│   │   ├── schemas/           Esquemas Pydantic
│   │   └── routers/           health, students
│   ├── migrations/            Migraciones de Alembic
│   ├── tests/                 Pruebas con pytest
│   ├── alembic.ini
│   ├── pyproject.toml         Configuración de Ruff y pytest
│   ├── requirements.txt       Dependencias de la API
│   └── requirements-dev.txt   + herramientas de desarrollo (pytest, ruff)
└── docs/                      Documentación del proyecto
```

## Ejecutar en local (Windows / PowerShell)

```powershell
cd backend
py -V:3.13 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt

Copy-Item .env.example .env      # y edita DATABASE_URL
alembic upgrade head             # crea las tablas
uvicorn app.main:app --reload
```

- Swagger UI: <http://127.0.0.1:8000/docs>
- Health check: <http://127.0.0.1:8000/health>

Si no defines `DATABASE_URL`, la API usa un SQLite local (`thesis_dev.db`).

## Revisiones de calidad (las mismas que ejecuta el CI)

```powershell
cd backend
ruff check .      # lint / análisis estático
pytest -v         # pruebas automáticas
```

## Endpoints actuales

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/health` | Estado del servicio (no usa la base de datos) |
| GET | `/api/students` | Listar estudiantes |
| GET | `/api/students/{id}` | Obtener un estudiante |
| POST | `/api/students` | Registrar un estudiante (409 si el email ya existe) |

## Flujo de trabajo

1. Crear una rama: `git checkout -b feature/nombre-del-cambio`
2. Ejecutar `ruff check .` y `pytest` antes de hacer push.
3. Abrir un pull request hacia `main`.
4. Hacer merge **solo si el CI está en verde** (`main` está protegida).
