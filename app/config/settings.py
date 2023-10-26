import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Waracle Cake API"
    postgres_host: str
    postgres_port: int = 5432
    postgres_user: str
    postgres_pass: str
    postgres_db: str

    model_config = SettingsConfigDict(
        env_file=f"{pathlib.Path(__file__).resolve().parent}\.env", extra="ignore"
    )
