import re
from textblob import TextBlob


class SentimentAnalysis:

    def __init__(self, tweet):
        self.tweet = tweet

    @staticmethod
    def clean_tweet(tweet):
        # Clean tweet text by removing links, special characters using simple regex statements
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    # only for english language
    def execute(self):
        tweet_data = self.clean_tweet(self.tweet)

        data = []

        # create TextBlob object of passed tweet text
        analysis = TextBlob(tweet_data)

        # set sentiment
        if analysis.sentiment.polarity > 0:
            data.append({'text': tweet_data, 'sentiment': 'positive'})
        elif analysis.sentiment.polarity == 0:
            data.append({'text': tweet_data, 'sentiment': 'neutral'})
        else:
            data.append({'text': tweet_data, 'sentiment': 'negative'})

        return data

if __name__ == "__main__":
	# calling main function
    SentimentAnalysis('hard to learn NLTK').execute()
