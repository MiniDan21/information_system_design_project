from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MAIN_HOST: str
    MAIN_PORT: int
    SECONDARY_HOST: str
    SECONDARY_PORT: int
    CORS_ALLOWED_IP: str

    @property
    def secondary_addr(self):
        return self.SECONDARY_HOST + ":" + str(self.SECONDARY_PORT)
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
