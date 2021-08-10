from app import app
import urllib.request,json
from .models import Source, Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["SOURCES_API_BASE_URL"]
source_url = app.config["SPECIFIC_SOURCE"]
topheadline_url = app.config["TOPHEADLINES_SOURCE"]
q=""
# TOP HEADLINES
def get_topheadlines(search):
    url = 'https://newsapi.org/v2/everything?q={}&apiKey={}' 
   
    get_article_details_url = url.format(search,api_key)
    with urllib.request.urlopen(get_article_details_url) as url:
        article_data = url.read()
        article_data_response = json.loads(article_data)

        article_object = None
        if article_data_response['articles']:
            articles_results_list = article_data_response['articles']
            article_data = process_articles_results(articles_results_list)    
    return article_data 


def get_article(id):
    """
     Function to get a single article
    """
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        article_data = url.read()
        article_data_response = json.loads(article_data)

        article_object = None
        if article_data_response:
            author = article_data_response.get('author')
            title = article_data_response.get('title')
            description = article_data_response.get('description')
            image = article_data_response.get('urlToImage')
            poster =  article_data_response.get('urlToImage') 
            date_published = article_data_response.get('publishedAt')
            content = article_data_response.get('content')

            article_object = Article(author,title,description,image,poster, date_published,content)
    return article_object 


# FUNCTIONS TO BE CALLED   
def process_articles_results(articles_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain movie details

    Returns :
        source_results: A list of movie objects
    '''
    articles_results = []
    for source_article in articles_list:
        author = source_article.get('author')
        title = source_article.get('title')
        description = source_article.get('description')
        image = source_article.get('urlToImage')
        poster =  source_article.get('urlToImage') 
        date_published = source_article.get('publishedAt')
        content = source_article.get('content')

        article_object =  Article(author,title,description,image,poster, date_published,content)
        articles_results.append(article_object)

    return articles_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain movie details

    Returns :
        source_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,language,country)
            source_results.append(source_object)

    return source_results

