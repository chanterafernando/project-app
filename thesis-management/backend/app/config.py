"""Configuración leída desde variables de entorno o desde el archivo .env.

Nunca escribas credenciales en el código: van en .env (excluido de Git)
o en las variables de entorno del servicio de hosting.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "Thesis Management API"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = os.getenv("APP_ENV", "development")

    # MySQL 8 en desarrollo/producción, por ejemplo:
    #   mysql+pymysql://thesis_user:CLAVE@localhost:3306/thesis_db
    # Si no se define, se usa un SQLite local para poder arrancar sin MySQL.
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./thesis_dev.db")


settings = Settings()
