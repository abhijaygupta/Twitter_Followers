import tweepy

ACCESS_TOKEN = '2173152326-yjL6K0n1OP0VRN2bkMhVnO5fj33QvGBrTGenOxh'
ACCESS_SECRET = 'RsBICRABzOwQCXs6QAnd6LgoAaA1V7Nvrplf2C9mEYBhZ'
CONSUMER_KEY = 'F9o8QImXyhOGWl1zixlXGQHDE'
CONSUMER_SECRET = '4shCSwYHyMnWpNYJQRUkgbUl2kjo9RhyW5xHzvfFK7eI67TV2a'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

s = 'thehungryladdoo';
s2 = 'SrBachchan';

user = api.get_user(s2)


for friend in user.friends():
   print friend.screen_name
print user.followers_count

print user.screen_name

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text