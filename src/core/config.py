from pydantic_settings import SettingsConfigDict, BaseSettings
class Config(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    is_debug: bool = True
    allowed_origins: list[str]
    secret_key: str
    algorithm: str
    hours_session: int
    model_config = SettingsConfigDict(env_file=".env")
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )
config = Config() 