from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    host_redis: str = "redis"
    port_redis: int = 6379

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """
    When you start your app, it makes sense to load your settings and then
    cache the data. Caching is an optimization technique that you can use
    in your applications to keep recent or often-used data in memory
    """
    settings = Settings()
    print(f"Loading settings for redis in: {settings.host_redis}")
    return settings
