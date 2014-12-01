import tweepy
import oauth

'''
create twitter api
'''
def getAPI(auth):
	api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
	return api
