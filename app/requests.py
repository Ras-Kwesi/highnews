import urllib.request,json
from .models import Movie

# Getting api key
api_key = None

news_url = None

def configure_request(app):
    global api_key,news_url
    api_key = app.config['API_KEY']
    news_url = app.config['NEWS_URL']



def request_news(source):
    '''
    Function to sort what content we want and
    convert our dictionary of news data to a list
    '''
    
    
