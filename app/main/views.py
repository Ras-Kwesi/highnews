from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():
    '''
    The function for our index html for what will be displayed
    '''

    title = "Welcome to Newsance"

    render_template('index.html',title=title)