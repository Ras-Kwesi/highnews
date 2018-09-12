from flask import render_template,request,redirect,url_for
from . import main
from ..models import Articles, Source


from ..requests import request_news, process_source_dict, request_articles, process_articles, request_article
@main.route('/')
def index():
    '''
    The function for our index html for what will be displayed
    '''

    general_news = request_news('general')
    sports_news = request_news('sports')
    business_news = request_news('business')
    entertainment_news = request_news('entertainment')
    science_news = request_news('science')
    tech_news = request_news('technology')
    title = "Newsance"

    return render_template('index.html',title=title, general=general_news, sports = sports_news, science = science_news, business = business_news, tech = tech_news, enter = entertainment_news)

@main.route('/articles/<author>')
def articles(author):
    '''
    The function to display our articles to the template
    '''
    author = request_articles(author)
    title = "Newsance"
    return render_template('articles.html', title = title , author = author)


@main.route('/articles/article/<author>')
def article(author):
    '''
    Function to get a single article
    '''

    article = request_article(author)
    title = f'{article.title}'

    return render_template('article.html', title = title)