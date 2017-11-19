import tweepy 

import time

#import user Twitter credentials from config.py
import config

consumer_key = config.twitter_credentials['CONSUMER_KEY']
consumer_secret = config.twitter_credentials['CONSUMER_SECRET']
access_token = config.twitter_credentials['ACCESS_TOKEN']
access_secret = config.twitter_credentials['ACCESS_SECRET']

#https://stackoverflow.com/questions/33498975/unable-to-stop-streaming-in-tweepy-after-one-minute


def oauth_authenticate():


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	print('Returning auth')
	return auth 


class MyStreamListener(tweepy.StreamListener):

	def __init__(self, start_time, time_limit):
		self.time = start_time
		self.limit = time_limit
		super(MyStreamListener, self).__init__()

	def on_data(self, data):
		print(data)
		if (time.time() - start_time) > self.limit:
			with open('twitter_data.txt', 'a') as tf: 
				tf.write(data)
				return True

		else:

			print('Completed the Twitter data stream')
			return False


	def on_error(self, status_code):
		if status_code == 420:
			return False
		


if __name__ == '__main__':

	start_time = time.time()
	
	l = MyStreamListener(start_time, 100)
	auth = oauth_authenticate()
	stream = tweepy.Stream(auth, l)
	
	stream.filter(track=['pycon', 'python'])

	






