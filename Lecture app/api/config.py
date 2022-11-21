import os

class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProdConfig(Config):
    pass
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    
class DevConfig(Config):
    pass
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/bart"
    
match os.getenv("ENV"):
    case "PRODUCTION":
        config = ProdConfig
    case _:
        config = DevConfig