# filename: fetch_recent_nvda_news.py

import os
from newsapi import NewsApiClient
import datetime

# Initialize the News API client
newsapi = NewsApiClient(api_key=os.environ.get('NEWSAPI_KEY'))

# Define the new accessible date range
start_date = datetime.datetime(2024, 6, 30) # adjusted according to API limitation
end_date = datetime.datetime.now()

# Fetch news articles about Nvidia from the accessible date range
nvda_news_within_limit = newsapi.get_everything(q='Nvidia',
                                                from_param=start_date.strftime('%Y-%m-%d'),
                                                to=end_date.strftime('%Y-%m-%d'),
                                                language='en',
                                                sort_by='relevancy')

# Print the titles and descriptions of the articles
for article in nvda_news_within_limit['articles']:
    print(f"Title: {article['title']}\nDescription: {article['description']}\n")