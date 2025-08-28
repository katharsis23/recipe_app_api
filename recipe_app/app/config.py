from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Database_Config(BaseSettings):
    database_host: str = Field(default="127.0.0.1", alias="DB_HOST") # for local developing
    database_port: int = Field(alias = "POSTGRES_PORT") #maybe change if 5433 if doesnt work
    database_user: str = Field(alias = "POSTGRES_USER")
    database_name: str = Field(alias = "POSTGRES_DB")
    database_password: str = Field(alias = "POSTGRES_PASSWORD")

    model_config=SettingsConfigDict(extra="ignore")


config = Database_Config()

#print(config.database_name)
#print(config.database_host)
#print(config.database_password)
#print(config.database_user)
#print(config.database_port)


    

