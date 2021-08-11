class Config:
    '''
    General configuration parent class
    '''
    SOURCES_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    SPECIFIC_SOURCE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    TOPHEADLINES_SOURCE = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    
    NEWS_API_KEY='271b6700bbff46808dcc9bbe2e093996'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}