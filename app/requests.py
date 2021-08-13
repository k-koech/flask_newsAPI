import urllib.request,json
from .models import Source, Article

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url, source_url
    api_key = app.config['NEWS_API_KEY']

    base_url = app.config["SOURCES_API_BASE_URL"]
    source_url = app.config["SPECIFIC_SOURCE"]
    topheadline_url = app.config["TOPHEADLINES_SOURCE"]

# TOP HEADLINES
def get_topheadlines(search):
    '''
    Function that gets the top headlines 
    '''

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

# GET SOURCES
def get_sources():
    '''
    Function that gets the json response  of the sources to our url request
    '''
    base_url = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results =process_results(source_results_list)
    return source_results

def get_source(id):
    '''
    Function that gets the specific news source
    '''
    get_source_details_url = source_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        movie_details_data = url.read()
        source_details_response = json.loads(movie_details_data)

        source_object = None
        if source_details_response['articles']:
            articles_results_list = source_details_response['articles']
            source_results = process_articles_results(articles_results_list)    
    return source_results


def get_article(id):
    """
     Function to get a single articles
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
            url =  article_data_response.get('url') 
            date_published = article_data_response.get('publishedAt')
            content = article_data_response.get('content')

            article_object = Article(author,title,description,image,url, date_published,content)
    return article_object 


# FUNCTIONS TO BE CALLED   
def process_articles_results(articles_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        source_results: A list of article objects
    '''
    articles_results = []
    for source_article in articles_list:
        author = source_article.get('author')
        title = source_article.get('title')
        description = source_article.get('description')
        image = source_article.get('urlToImage')
        url =  source_article.get('url') 
        date_published = source_article.get('publishedAt')
        content = source_article.get('content')

        article_object =  Article(author,title,description,image,url, date_published,content)
        articles_results.append(article_object)

    return articles_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
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

