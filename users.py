import tweepy
import oauth

auth = oauth.createAuth()
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

user = api.get_user('424513038')
print user['name'] + ' ' + user['description']
print user['status']
