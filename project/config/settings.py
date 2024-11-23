from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings(env):
    settings = Settings()

    if env == "test":
        env_file_path = os.path.join(os.getcwd(), "test_env.env")
    elif env == "prod":
        env_file_path = os.path.join(os.getcwd(), ".env")
    else:
        raise ValueError("Invalid environment specified")

    try:
        load_dotenv(dotenv_path=env_file_path)
        return Settings()
    except FileNotFoundError:
        raise ValueError(f"Environment file {env_file_path} not found")
