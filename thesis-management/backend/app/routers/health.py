from datetime import UTC, datetime

from fastapi import APIRouter

from app.config import settings

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="Estado del servicio",
    description="Comprueba que la API está en línea. No consulta la base de datos.",
)
def health() -> dict:
    return {
        "status": "ok",
        "service": "thesis-management-api",
        "version": settings.APP_VERSION,
        "timestamp": datetime.now(UTC).isoformat(),
    }
