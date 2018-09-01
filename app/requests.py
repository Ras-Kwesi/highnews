import urllib.request,json
from .models import Articles,Source

# Getting api key
api_key = None

articles_url = None

news_url = None

def configure_request(app):
    global api_key,news_url,articles_url
    api_key = app.config['API_KEY']
    news_url = app.config['NEWS_URL']
    articles_url = app.config['ARTICLES_URL']


def request_news(category):
    '''
    Function to sort whhat our api call has returned and pick the sources list
    for sorting out
    '''

    request_news_url = news_url.format(category,api_key)
    
    with urllib.request.urlopen(request_news_url) as url:
        request_news_data = url.read()
        request_news_response = json.loads(request_news_data)

        source_list = None

        if request_news_response['sources']:
            source_dict_list = request_news_response['sources']
            source_list = process_source_dict(source_dict_list)

    return source_list


def process_source_dict(sources_category_list):
    '''
    Function to get the values of a news source dictionary and make them an object of the
    source class
    '''

    source_list = []
    for news_source in sources_category_list:
        id = news_source.get('id')
        name = news_source.get('name')
        category = news_source.get('category')
        url = news_source.get('url')
        language = news_source.get('language')
        country = news_source.get('country')
        description = news_source.get('description')
        
        source_object = Source(id,name,category,url,language,country,description)

        source_list.append(source_object)

    return source_list

def request_articles(source_news_dict_list):
    '''
    Function to get the values of the news source dictionary keys and converting them to
    an object of the articles class
    '''

    articles_list = []
    for article in source_news_dict_list:
        