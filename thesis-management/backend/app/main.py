from fastapi import FastAPI

from app.config import settings
from app.routers import health, students

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "API para la gestión del proceso de titulación (tesis, tutores, revisores y defensas)."
    ),
)

app.include_router(health.router)
app.include_router(students.router)
