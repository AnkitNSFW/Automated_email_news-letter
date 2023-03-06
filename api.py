from newsdataapi import NewsDataApiClient
from config import newsdata_api_key
from pprint import pprint

# Setting up API Client
api = NewsDataApiClient(apikey=newsdata_api_key)

def api_news(topic):
    response = api.news_api( q= topic, language="en")
    return response["results"]

if __name__ == "__main__":
    pprint(api_news("everything"))