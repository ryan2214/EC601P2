# -*- coding:utf-8 -*-
import os
from TwitterAPI import TwitterAPI

# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a NLP client
client = language_v1.LanguageServiceClient()

SEARCH_TERM = '#Trump'

api = TwitterAPI(os.environ.get("consumer_key"),
                 os.environ.get("consumer_secret"),
                 auth_type='oAuth2')

SENTI_NUM = 0
TEXT_TEMP = u' '
#Search x tweets about Trump

r = api.request('search/tweets', {'q': SEARCH_TERM,'count':100, 'tweet_mode':"extended"})

for item in r:
    if item['lang'] == 'en' :
# The text to analyze
        if 'extended_tweet' in item:
            text = item['extended_tweet']['full_text']
        if 'retweeted_status' in item:
            text = item['retweeted_status']['full_text']
        elif 'full_text' in item:
            text = item['full_text']
        elif 'text' in item:
            text = item['text']

        SENTI_NUM += 1
        TEXT_TEMP = TEXT_TEMP + text

document = language_v1.Document(content=TEXT_TEMP, type_=language_v1.Document.Type.PLAIN_TEXT)
SENTI_RESULT = client.analyze_sentiment(request={'document': document}).document_sentiment.score

print("SentimentResult: {}".format(SENTI_RESULT))
