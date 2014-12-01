'''
https://gist.github.com/yanofsky/5436496
'''

import tweepy
import oauth

def get_all_tweets(screen_name):
	auth = oauth.createAuth()
	api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

	alltweets = []
	new_tweets = api.user_timeline(screen_name,count = 10)
	alltweets.extend(new_tweets)

	for tweet in alltweets:
		print tweet['text']


if __name__ == '__main__':
	get_all_tweets('20998647')
