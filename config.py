import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_URL = 'https://newsapi.org/v2/everything?q={}apiKey={}'
    API_KEY = '51664d7eabf94215b7a3a91eab4f0cad'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}