# filename: fetch_nvda_news.py

import os
from newsapi import NewsApiClient
import datetime

# Initialize the News API client.
newsapi = NewsApiClient(api_key=os.environ.get('NEWSAPI_KEY'))

# Define the date range
end_date = datetime.datetime(2024, 6, 23)
start_date = end_date - datetime.timedelta(days=30)

# Fetch news articles about Nvidia
nvda_news = newsapi.get_everything(q='Nvidia',
                                   from_param=start_date.strftime('%Y-%m-%d'),
                                   to=end_date.strftime('%Y-%m-%d'),
                                   language='en',
                                   sort_by='relevancy')

# Print the titles and descriptions of the first 10 articles
for article in nvda_news['articles'][:10]:
    print(f"Title: {article['title']}\nDescription: {article['description']}\n")