import tweepy
from credentials import keys

'''
keys are represented in a dictionary.
initialize the auth object with keys 
'''
def createAuth():
	auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
	auth.secure = True
	auth.set_access_token(keys['access_token'], keys['access_token_secret'])
	
	return auth

if __name__ == '__main__':
	createAuth()
