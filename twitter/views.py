from django.http.response import HttpResponse
from django.shortcuts import render
import oauth2 as oauth
import cgi
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import urlparse
import tweepy


request_token_url = 'https://twitter.com/oauth/request_token'
access_token_url = 'https://twitter.com/oauth/access_token'
authorize_url = 'https://twitter.com/oauth/authorize'
app_only_authentiation_url ="https://api.twitter.com/oauth2/token"
oauth_token = ""
oauth_token_secret =""
user_id = ""


def hello(request):
    return render(request, "index.html")

def newhello(request):
    # Step 1. Use the request token in the session to build a new client.
    print request
    print request.session
    oauth_verifier = request.GET['oauth_verifier']
    oauth_token = request.GET['oauth_token']
    
    token = oauth.Token(oauth_token,
        oauth_verifier)
    token.set_verifier(oauth_verifier)
     
    consumer = oauth.Consumer(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET_KEY)
    client = oauth.Client(consumer, token)
     
    # Step 2. Request the authorized access token from Twitter.
    resp, content = client.request(access_token_url, "POST")
    if resp['status'] != '200':
        print content
        raise Exception("Invalid response from Twitter.")
    access_token = dict(cgi.parse_qsl(content))
    #print access_token
    screen_name =  access_token['screen_name']
    global oauth_token_secret
    oauth_token_secret = access_token['oauth_token_secret']
    global user_id
    user_id = access_token['user_id']
    global oauth_token
    oauth_token = access_token["oauth_token"]
#     print "Screen name ", screen_name
#     print "oauth_token_secret", oauth_token_secret
#     print "user_id", user_id
#     print "oauth_token", oauth_token
    return render(request, "ujjwal.html", {"screen_name": screen_name})

def post(request):
    print "posting something"
    if request.method == "POST":
        text_to_post = request.POST['text_to_post']
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET_KEY)
        print " now in post", oauth_token
        print " now in post", oauth_token_secret
        auth.set_access_token(oauth_token, oauth_token_secret)
        api = tweepy.API(auth)
        status = text_to_post
        api.update_status(status=status)
        pub = api.user_timeline(user_id, count=10)
        return render_to_response("tweets.html", {"tweets": pub})

def login(request):
    consumer = oauth.Consumer(key=settings.TWITTER_CONSUMER_KEY,
                               secret=settings.TWITTER_CONSUMER_SECRET_KEY)
    #token = oauth.Token(key=settings.TWITTER_CONSUMER_KEY,
    #                    secret=settings.TWITTER_CONSUMER_SECRET_KEY)
    client = oauth.Client(consumer)
    
    # Step 1: Get a request token. This is a temporary token that is used for 
    # having the user authorize an access token and to sign the request to obtain 
    # said access token.
    
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response %s." % resp['status'])
    request_token = dict(urlparse.parse_qsl(content))
    print "Request Token:"
    print "    - oauth_token        = %s" % request_token['oauth_token']
    print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
    print 
    
    
    
    print "Go to the following link in your browser:"
    print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
    print 
    
    redirect_url = "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
    print redirect_url
    return HttpResponseRedirect(redirect_url)


