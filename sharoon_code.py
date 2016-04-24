import json
import tweepy
import time

ACCESS_TOKEN = '2173152326-yjL6K0n1OP0VRN2bkMhVnO5fj33QvGBrTGenOxh'
ACCESS_SECRET = 'RsBICRABzOwQCXs6QAnd6LgoAaA1V7Nvrplf2C9mEYBhZ'
CONSUMER_KEY = 'F9o8QImXyhOGWl1zixlXGQHDE'
CONSUMER_SECRET = '4shCSwYHyMnWpNYJQRUkgbUl2kjo9RhyW5xHzvfFK7eI67TV2a'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

'''
user = api.get_user('twitter')

print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name
   
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    process_friend(friend)
'''
s = 'thehungryladdoo'
s2 = 'SrBachchan'

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name=s2).pages():
    ids.extend(page)
    time.sleep(5)

print len(ids)
print ids

user = api.get_user(id=ids[0])
print user.screen_name
'''
for friend in user.friends():
   print friend.screen_name
print user.followers_count

print user.screen_name

print ' '
print user.location'''
