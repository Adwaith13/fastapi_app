from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_username:str
    database_password:str
    database_host:str
    database_dbname:str
    oauth2_secretkey:str
    algorithm:str
    access_token_expire_minutes:int
    
    class Config:
        env_file = ".env"
        
settings = Settings()