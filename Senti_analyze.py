# -*- coding:utf-8 -*-
from TwitterAPI import TwitterAPI, TwitterPager

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a NLP client
client = language.LanguageServiceClient()

SEARCH_TERM = '#Trump'

consumer_key = ""
consumer_secret = ""

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 auth_type='oAuth2')



#Search 10 tweets about Trump

r = api.request('search/tweets', {'q': SEARCH_TERM,'count':10})

for item in r:
# The text to analyze
    text = item['text'].encode('utf-8')
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

print('\nQUOTA: %s' % r.get_quota())




