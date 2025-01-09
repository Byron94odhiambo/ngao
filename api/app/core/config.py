from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "NGAO Security Platform"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "ngao-security-platform-secret-key-2025"  # Fixed secret key for development
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # Database
    POSTGRES_SERVER: str = "postgres"
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "securitydb"

    class Config:
        case_sensitive = True

settings = Settings()
