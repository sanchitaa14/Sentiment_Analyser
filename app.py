import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Twitter API credentials
# bearer token AAAAAAAAAAAAAAAAAAAAAKNJvQEAAAAAEUI6AHQDaF%2FZuqvG6s32IZTRq1A%3DSthW0Onv8dZ6Y2yhzZFsRGLE0aYCEiQ6nEsyswCHq58sN7ZMm2
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKNJvQEAAAAAEUI6AHQDaF%2FZuqvG6s32IZTRq1A%3DSthW0Onv8dZ6Y2yhzZFsRGLE0aYCEiQ6nEsyswCHq58sN7ZMm2'

# Set up Tweepy client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.route('/sentiment', methods=['GET'])
def sentiment():
    topic = request.args.get('topic')
    if topic:
        # Fetch recent tweets on the topic
        query = f'{topic} -is:retweet lang:en'
        tweets = client.search_recent_tweets(query=query, max_results=100)
        tweets_data = tweets.data if tweets.data else []
        
        sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
        
        # Analyze sentiment of each tweet
        for tweet in tweets_data:
            sentiment_score = analyzer.polarity_scores(tweet.text)
            if sentiment_score['compound'] >= 0.05:
                sentiments['positive'] += 1
            elif sentiment_score['compound'] <= -0.05:
                sentiments['negative'] += 1
            else:
                sentiments['neutral'] += 1
        
        return jsonify(sentiments)
    return jsonify({'error': 'No topic provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
