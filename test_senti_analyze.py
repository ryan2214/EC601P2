from TwitterAppPrototype import *

# test about TwitterAPI
twitter = TwitterAPI()

def test_TwitterAPI_analyze_sentiment():
    text = "Have a nice day!"
    score = twitter.analyze_sentiment(text)
    assert score > 0.25 # positive sentiment
