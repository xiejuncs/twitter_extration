from tweepy.streaming import StreamListener
from tweepy import Stream

import oauth

class StdOutListener(StreamListener):
	def on_data(self, data):
		print(data)
		return True

	def on_error(self, status):
		print(status)

if __name__ == '__main__':
	l = StdOutListener()
	auth = oauth.createAuth()

	stream = Stream(auth, l)
	stream.filter(track=['basketball'])
