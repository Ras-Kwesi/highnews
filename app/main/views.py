from flask import render_template,request,redirect,url_for
from . import main
from ..models import Articles, Source


from ..requests import request_news, process_source_dict
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

    return render_template('index.html',title=title, general = general_news, sports = sports_news, science = science_news, business = business_news, tech = tech_news, enter = entertainment_news)
