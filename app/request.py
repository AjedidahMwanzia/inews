from app import app
import urllib.request,json
from .models import source
from instance.config import NEWS_API_KEY
from newsapi import NewsApiClient

Source = source.Source


# Getting api key
source_api_key = NewsApiClient(api_key=NEWS_API_KEY)

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(source_api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
  
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results