import urllib.request,json
from .models import Articles,Source,Article

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

def request_articles(author):
    '''
    Function to get the list of articles dictionary and make the from
    json to python dicts before conversion to objects
    '''

    request_articles_url = articles_url.format(author, api_key)

    with urllib.request.urlopen(request_articles_url) as url:
        request_articles_data = url.read()
        request_articles_response = json.loads(request_articles_data)

        articles_list = None

        if request_articles_response['articles']:

            article_dict_list = request_articles_response['articles']
            articles_list = process_articles(article_dict_list)

    return articles_list

def request_article(author):
    '''
    Function to display a single article
    '''

    request_article_url = articles_url.format(author, api_key)

    with urllib.request.urlopen(request_article_url) as url:
        request_article_data = url.read()
        request_article_response = json.loads(request_article_data)

        article_object = None

        if request_article_response:
            author = request_article_response.get('author')
            title = request_article_response.get('title')
            description = request_article_response.get('description')
            url = request_article_response.get('url')
            urlToImage = request_article_response.get('urlToImage')

            article_object = Article(author,title,description,urlToImage,url)

    return article_object





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

def process_articles(source_news_dict_list):
    '''
    Function to get the values of the news source dictionary keys and converting them to
    an object of the articles class
    '''

    articles_list = []
    for article in source_news_dict_list:
        title = article.get('title')
        author = article.get('author')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')


        # for id in d.get('sources',()):
        #     return ''

        # source = None
        #
        # if article == 'source':
        #     for key in article:
        #         source = key.get('id')
        #
        #     return source


        article_object = Articles(title,author,description,url,urlToImage,publishedAt)

        articles_list.append(article_object)

    return articles_list


