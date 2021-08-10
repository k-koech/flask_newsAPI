from flask import render_template,request,redirect,url_for
from app import app
from .models import Source, Article
from .requests import get_sources, get_source, get_topheadlines

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    news_sources = get_sources()

    search='tokyo'
    trending = get_topheadlines(search)

    title = 'Home - News Sources'

    return render_template('index.html', title = title, sources = news_sources, trending=trending)


@app.route('/source/<id>')
def source(id):
    '''
    View source page function that returns the news_sourcesindex page and its data
    '''
    news_sources = get_sources()
    source_details = get_source(id)
    title = 'Source - '+id
    source = id.upper()

    return render_template('source.html',sources = news_sources, source=source, source_details=source_details)


@app.route('/404')
def article():
    '''
    View source page function that returns the index page and its data
    '''
    return render_template('404.html')