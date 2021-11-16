import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    # Swagger
    RESTX_MASK_SWAGGER = False
    #SERVER_NAME = '0.0.0.0:5001'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)