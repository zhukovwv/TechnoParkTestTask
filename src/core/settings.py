from collections.abc import AsyncGenerator

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file="../.env",
        extra="ignore",
    )

    # --- App settings ---
    APP_NAME: str = Field(default="Cost Calculator Service")
    APP_DESCRIPTION: str = Field(default="Service for calculating product cost")
    SWAGGER_PATH: str = Field(default="/docs")

    # --- PostgreSQL settings ---
    PG_HOST: str = Field(...)
    PG_PORT: int = Field(default=5432)
    PG_DB: str = Field(...)
    PG_USER: str = Field(...)
    PG_PASSWORD: str = Field(...)

    # --- Logging ---
    LOG_ENABLED: bool = Field(default=True)
    LOG_LEVEL: str = Field(default="INFO")

    @property
    def pg_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.PG_USER}:"
            f"{self.PG_PASSWORD}@{self.PG_HOST}:"
            f"{self.PG_PORT}/{self.PG_DB}"
        )

    async def get_db_engine(self) -> AsyncGenerator[AsyncEngine, None]:
        """
        Async SQLAlchemy engine generator.
        """
        engine = create_async_engine(self.pg_url, echo=False)
        try:
            yield engine
        finally:
            await engine.dispose()


settings = Settings()
