import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'fridah'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

     #email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'fridahalwanga6@gmail.com'
    MAIL_PASSWORD = '38642204'
    SUBJECT_PREFIX = 'blog'
    SENDER_EMAIL = 'fridahalwanga6@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blog'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blog'
    DEBUG = True
    ENV = 'development'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}