import os

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    HOST  = '0.0.0.0'
    PORT  = int(os.getenv('PORT', '5000'))
    #Database Configuration


