# twitter
Twitter app oauth

This is a basic Django APP which does the below stuff

         Create a login button in the home page
·        A user should be authenticated using Twitter API (oAuth) - you can use any twitter python libs
·        After a successful login (using Twitter API) print the users name in a new page. This page should also have a textbox and a submit button.
·        When the user posts a message to Twitter API, it should add a new Tweet as the logged in user.
·        After a tweet is added, you need to be able to verify that the new tweet was indeed added by listing the user’s last 10 tweets.

Python packages needed for this to work are:
basicauth==0.2
oauth==1.0.1
oauth2==1.5.211
oauthlib==0.7.2
tweepy==3.3.0
