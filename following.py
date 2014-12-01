import tweepy
import oauth

'''
Get ids of the users I follow
'''
def getIds():
	auth = oauth.createAuth()
	api = tweepy.API(auth)
	
	friends_ids = api.friends_ids()
	return friends_ids

'''
Get detailes of the users I follow
'''
def getFriends():
	auth = oauth.createAuth()
	api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

	friends = api.friends()
	return friends

if __name__ == '__main__':
	ids = getIds()
	for i in ids:
		print i
