'''
https://gist.github.com/yanofsky/5436496
'''
import tweepy
import tweepy_helper
import oauth

'''
reference: https://dev.twitter.com/rest/reference/get/statuses/user_timeline
allowed_param:'id', 'user_id', 'screen_name', 'since_id'
'''
def get_all_tweets(user_identifier, api, c = 10):
	alltweets = []
	tweets = api.user_timeline(user_identifier, count = c)
	alltweets.extend(tweets)
	return alltweets

if __name__ == '__main__':
	auth = oauth.createAuth()
	api = tweepy_helper.getAPI(auth)
	alltweets = get_all_tweets("BobbyDWeather", api)
	for tweet in alltweets:
		print tweet['text']
