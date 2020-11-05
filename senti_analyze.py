# -*- coding:utf-8 -*-
from TwitterAPI import TwitterAPI

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a NLP client
client = language.LanguageServiceClient()

SEARCH_TERM = '#Trump'

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 auth_type='oAuth2')

SENTI_RESULT = 0
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

document = types.Document(content=textTemp, type=enums.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(document=document).document_sentiment

SENTI_RESULT = sentiment.score

print("SentimentResult: {}".format(SENTI_RESULT))
