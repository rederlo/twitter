import tweepy

CONSUMER_KEY = 'hJNK668aplCAp2X67I7oeORjq'
CONSUMER_SECRET = 'NydUfEtjkMgYLgxoddziy3NpMs6o0NoDOWtT0a7f9UjLmtF29s'
ACCESS_TOKEN = '2932126434-yGmt2CNv0KhBmFJ7TgEfzdcC7fcZQvk2Xc2OjJI'
ACCESS_TOKEN_SECRET = 'ciMRGTE98iwTRLR4sovfdtpjwTTV2C3M4bkjXkN5mCpwk'



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

