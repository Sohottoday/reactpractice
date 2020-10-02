import tweepy

consumer_key = 'Mwo8KsPPsUH2a2RAuBAGqhOtD'
consumer_secret = 'uwaZjK3nNCZjUbkUiMRLNsrYH9P0yo6zt2VbE2Ctgk08QtGqZU'
twitter_access_token = '1311709615923445760-Khswk7BPmSD4GFUDdp2EGlGAZJAjIv'
twitter_access_secret = 'DD1rtTErJUOfVGjfjsL5ahDKm0ENy9IVxM4BLno0Cshoa'

#twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_consumer_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)
twitter_api = tweepy.API(auth)

query = "영화"
api_result = []

tweet = twitter_api.search(query)

for tw in tweet:
    api_result.append(tw.text)

#print(api_result)
for aaa in api_result:
    print(aaa)


