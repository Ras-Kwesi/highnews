import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')



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