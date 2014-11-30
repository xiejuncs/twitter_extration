import tweepy
import IOUtils

def createAuth():
	path = "/home/jun/open_source/credentials/twitter/twitter_credential.txt"
	ret = IOUtils.readFiles(path) 

	auth = tweepy.OAuthHandler(ret[0], ret[1])
	auth.secure = True
	auth.set_access_token(ret[2], ret[3])
	
	return auth
