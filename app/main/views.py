from flask import render_template,request,redirect,url_for
from . import main
from ..models import Articles, Source


from ..requests import request_news, process_source_dict
@main.route('/')
def index():
    '''
    The function for our index html for what will be displayed
    '''

    title = "Welcome to Newsance"

    return render_template('index.html',title=title)