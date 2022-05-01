from app import app
from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results


...
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('original_name')
        description = news_item.get('description')
        url = source_item.get('url')
       
        

        if id:
            news_object = News(id,title,name,description,url)
            news_results.append(news_object)

    return news_results
