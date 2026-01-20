from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class AppSettings(BaseSettings):
    skip_top: int = Field(default=5, ge=0)
    remove_first_row: bool = True

    excel_path: str = "caminhoexcel"
    parquet_th: str = "caminhoparquet"
    database_url: str = "caminhodatabase"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = AppSettings()