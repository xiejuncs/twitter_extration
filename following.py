import tweepy
import tweepy_helper
import oauth

'''
Get ids of the users I follow
'''
def getIds(api):
	friends_ids = api.friends_ids()
	return friends_ids['ids']

'''
Get detailes of the users I follow
def getFriends(api):
	friends = api.friends()
	return friends
'''

if __name__ == '__main__':
	auth = oauth.createAuth()
        api = tweepy_helper.getAPI(auth)
	ids = getIds(api)
	for i in ids:
		print i
