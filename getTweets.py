import tweepy
#import json
import sys

access_token = "3107483956-JoAgiNYQeReWnx79zMPOw2uFHrmJvybHVA5k1Kz"
access_token_secret = "G442KdW1jf7GWx55q3qwB5h6FqteZMyAq2JRm9FgtdvGu"
consumer_key = "MzX8LWtTildWh99jESPrDTklV"
consumer_secret = "EswSb2jNPCqdQdLs87rFSKLzOIYHymtp6MPM10i0btUzYpvx6X"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#num = 0
for tweet in tweepy.Cursor(api.search, q=sys.argv[1:], lang='fr', tweet_mode='extended').items(100):
#    num=num+1
    if 'retweeted_status' in dir(tweet):
        tweets=tweet.retweeted_status.full_text
    else:
        tweets=tweet.full_text

#        data = {}
#        data['username'] = tweet.user.name
#        data['text'] = tweets
#        json_data = json.dumps(data, ensure_ascii=False)

#        parsed = json.loads(json_data)
#        print parsed

#    print num
    print tweets.encode('utf-8')
#    print tweet.user.name.encode('utf-8')
#    print tweet.created_at
    print "-------------------------------"
