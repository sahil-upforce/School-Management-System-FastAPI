import os
from pathlib import Path

from dotenv import load_dotenv


def load_env_files():
    project_path = Path(".")

    local_env_path = project_path / ".env.local"
    prod_env_path = project_path / ".env.prod"

    if local_env_path.is_file():
        load_dotenv(dotenv_path=local_env_path)
    elif prod_env_path.is_file():
        load_dotenv(dotenv_path=prod_env_path)
    else:
        raise FileNotFoundError(
            "Please add .env.local or .env.prod file and get reference from .env.example file"
        )


class Settings:
    # Load Env Files
    load_env_files()

    # Project Configurations
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")
    DEBUG: bool = os.getenv("DEBUG", False)

    # Database Configurations
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv(
        "POSTGRES_PORT", 5432
    )  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # JWT Configurations
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    REFRESH_TOKEN_EXPIRE_MINUTES = os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", 60 * 24)
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")


settings = Settings()
