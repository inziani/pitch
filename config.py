from os import environ, path

class Config:
  SECRET_KEY ='98d704bf8b0febc605b80b105439fd17'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///pitches.db'
  FLASK_ENV = 'development'

  @staticmethod
  def create_app():
    pass


class DevConfig(Config):
  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'sqlite:///pitches.db'
  

class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///pitches.db'

class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///pitches.db'

config = {
  'development' : DevConfig,
  'testing' : TestingConfig,
  'production' : ProdConfig,
  'default': DevConfig
}
