import tweepy
import following
import tweet_dumper
import tweepy_helper
import oauth
import IOUtils

auth = oauth.createAuth()
api = tweepy_helper.getAPI(auth)

# Get a list of following friends
friend_ids = following.getIds(api)

# for each following id
alltweets = []
for friend_id in friend_ids:
	print 'screen_name ' + str(friend_id)
	tweets = tweet_dumper.get_all_tweets(friend_id, api)
	print 'tweet size is ' + str(len(tweets))
	for tweet in tweets:
		alltweets.append(tweet['text'].replace('\n', ' '))

print "all tweets size is " + str(len(alltweets))
for tweet in alltweets:
	print tweet

IOUtils.write('weather.txt', alltweets)
