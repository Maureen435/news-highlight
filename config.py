import os

class Config:

    NEWS_SOURCES_BASE_URL ='http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-06&sortBy=publishedAt&apiKey={}'
    ARTICLES_BASE_URL ='http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}'
    NEWS_API_KEY =os.environ.get('NEWS_API_KEY')
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}