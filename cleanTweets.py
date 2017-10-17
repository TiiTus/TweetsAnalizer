import re


def cleanTweets(tweet):
    # Remove URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet)
    # Remove @username
    tweet = re.sub('@[^\s]+', '', tweet)
    # Remove emojis
    emojis = re.compile(U'['
                        U'\U0001F300-\U0001F64F'
                        U'\U0001F680-\U0001F6FF'
                        U'\U0001F1E0-\U0001F1FF'
                        U'\u2000-\u2FFF'
                        U'\u2600-\u26FF\u2700-\u27BF]+',
                        re.UNICODE)
    tweet = emojis.sub(r'', tweet)
    # Remove white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    # Change special entities
    tweet = re.sub('&amp;', '&', tweet)
    tweet = re.sub('&gt;', '>', tweet)
    tweet = re.sub('&lt;', '<', tweet)
    # Remove additional tab, space, etc
    tweet = tweet.strip(' \t\n\r')
    return tweet


with open('tweets.txt', encoding='utf8') as file, open('cleanedTweets.txt', 'w', encoding='utf8') as cleanfile:
    for line in file:
        if not line.strip(): continue
        cleanTweet = cleanTweets(line)
        cleanfile.write(cleanTweet + '\n')
