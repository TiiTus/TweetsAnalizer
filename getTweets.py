import tweepy

access_token = "3107483956-JoAgiNYQeReWnx79zMPOw2uFHrmJvybHVA5k1Kz"
access_token_secret = "G442KdW1jf7GWx55q3qwB5h6FqteZMyAq2JRm9FgtdvGu"
consumer_key = "MzX8LWtTildWh99jESPrDTklV"
consumer_secret = "EswSb2jNPCqdQdLs87rFSKLzOIYHymtp6MPM10i0btUzYpvx6X"

#Connection to API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

keyword=input("Which word do you want to search ?  ")
number=input("How many tweets do you want ?  ")
nb=int(number)

file=open("data.txt", "wb")

for tweet in tweepy.Cursor(api.search, q=keyword, lang='fr', tweet_mode='extended').items(nb):

    if 'retweeted_status' in dir(tweet):
        tweets=tweet.retweeted_status.full_text
    else:
        tweets=tweet.full_text

#Write tweets in file data.txt
    file.write(tweets.encode('utf-8'))
    my_str = "\n"
    my_str_as_bytes = str.encode(my_str)
    file.write(my_str_as_bytes)

file.close()
