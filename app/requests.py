import urllib.request,json
from .models import Articles,Source

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

    request_news_url = news_url.format(source, api_key)
    with urllib.request.urlopen(request_news_url) as url:
        request_news_data = url.read()
        request_news_response = json.loads(request_news_data)

        news_call_response = None

        if request_news_response['sources']:
            source_dict_list = request_news_response['sources']
            news_list = process_source_dict(source_dict_list)

    return news_list