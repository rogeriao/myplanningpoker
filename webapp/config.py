from os import path
class Config(object):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(
        path.pardir,
        'database.db'
    )

class UATConfig(Config):
    pass

class ProdConfig(Config):
    pass
