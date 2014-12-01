import tweepy
import tweepy_helper
import oauth

auth = oauth.createAuth()
api = tweepy_helper.getAPI(auth)

user = api.get_user('424513038')
print user['name'] + ' ' + user['description']
print user['status']
