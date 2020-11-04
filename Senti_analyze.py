# -*- coding:utf-8 -*-
from TwitterAPI import TwitterAPI, TwitterPager

# Imports the Google Cloud client library
#from google.cloud import language
#from google.cloud.language import enums
#from google.cloud.language import types

# Instantiates a NLP client
client = language.LanguageServiceClient()

SEARCH_TERM = '#Trump'

consumer_key = ${{secrets.GOOGLE_CONSUMER_KEY}}
consumer_secret = ${{secrets.GOOGLE_CONSUMER_SECRET}}

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 auth_type='oAuth2')

sentiResult = 0
sentiNum = 0
textTemp = u' '
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

        sentiNum += 1
        textTemp = textTemp + text

document = types.Document(content=textTemp, type=enums.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(document=document).document_sentiment

sentiResult = sentiment.score

print("SentimentResult: {}".format(sentiResult))
