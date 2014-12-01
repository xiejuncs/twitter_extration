import tweepy
import following
import tweet_dumper

# Get a list of following friends
friend_ids = following.getIds()

# for each following id
alltweets = []
for friend_id in friend_ids:
	print 'screen_name ' + str(friend_id)
	tweets = tweet_dumper.get_all_tweets(friend_id)
	print 'tweet size is ' + str(len(tweets))
	for tweet in tweets:
		alltweets.append(tweet['text'])

print "all tweets size is " + str(len(alltweets))
for tweet in alltweets:
	print tweet
