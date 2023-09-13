class Settings:
    # Project Configurations
    PROJECT_NAME: str = "School Management System"
    PROJECT_VERSION: str = "1.0.0"

    # Database Configurations
    DATABASE_URL = "sqlite:///./student_management_system.db"
    DEBUG = True

    # JWT Configurations
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 min
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day
    JWT_ALGORITHM = "HS256"
    JWT_SECRET_KEY = "___PRIVET_KEY_BEGINS__PRIVATE_KEY__PRIVATE_KEY_ENDS___"
    JWT_REFRESH_SECRET_KEY = "___REFRESH_PRIVET_KEY_BEGINS__REFRESH_PRIVATE_KEY__REFRESH_PRIVATE_KEY_ENDS___"

    # For postgreSQL
    # POSTGRES_USER: str = os.getenv("POSTGRES_USER", "pg_user")
    # POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
    # POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    # POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    # POSTGRES_DB: str = os.getenv("POSTGRES_DB", "db_name")
    # DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
