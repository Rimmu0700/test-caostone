from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("../../.env", ".env"), extra="ignore"
    )

    app_env: str = "development"
    app_port: int = 8000

    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "usada_bali"
    db_user: str = ""
    db_password: str = ""

    curator_email: str = ""
    curator_password: str = ""

    @property
    def database_url(self) -> URL:
        return URL.create(
            drivername="postgresql+psycopg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()