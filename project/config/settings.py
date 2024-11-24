from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    database_url: str
    secret_key: str

def get_settings(env):
#    settings = Settings()

    if env == "test":
        env_file_path = "test_env.env"
    elif env == "prod":
        env_file_path = ".env"
    else:
        raise ValueError("Invalid environment specified")
    try:
        load_dotenv(dotenv_path=env_file_path)
        database_url = os.getenv('DATABASE_URL')
        secret_key = os.getenv("SECRET_KEY")
        setting = Settings(database_url=database_url, secret_key=secret_key)
        return Settings()
    except FileNotFoundError:
        raise ValueError(f"Environment file {env_file_path} not found")
