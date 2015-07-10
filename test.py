import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

pub = api.user_timeline(2932126434, count=10)
for i in pub:
	#print dir(i)
	print "-----------"
	print i.text
	print i.created_at
#status = "Again Testing!"
#api.update_status(status=status)

