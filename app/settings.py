try:
    from pydantic_settings import BaseSettings
except ModuleNotFoundError:  # fallback for pydantic<2
    from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Preventive Maintenance API"
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
