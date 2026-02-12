from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    my_secret_password_to_wallet: str

    class Config:
        env_file = ".env"


settings = Settings()
