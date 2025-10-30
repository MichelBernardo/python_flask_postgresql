import os
from dotenv import load_dotenv


load_dotenv()  # Loads the variables from the .env file into the enviroment


class Config:
    """
        Basic application settings.
    """

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_test')
    DEBUG = False
    TESTING = False

    # Database configurations using environment variables
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class DevelopmentConfig(Config):
    """
        Settings for the development environment.
    """
    DEBUG = True
    PORT = 5000


class ProductionConfig(Config):
    """
        Settings for the production environment.
    """
    DEBUG = False
    PORT = 8000


config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}