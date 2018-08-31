import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    API_KEY = os.environ.get('51664d7eabf94215b7a3a91eab4f0cad')



class ProdConfig(Config):
    '''
    Production  configuration child class
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}