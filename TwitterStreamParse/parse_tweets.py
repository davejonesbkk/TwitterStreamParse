

import smtplib, json, tweepy, time, tweepy

#import user Twitter twitter_credentialstials from config.py
import config

consumer_key = config.twitter_credentials['CONSUMER_KEY']
consumer_secret = config.twitter_credentials['CONSUMER_SECRET']
access_token = config.twitter_credentials['ACCESS_TOKEN']
access_secret = config.twitter_credentials['ACCESS_SECRET']
gmail_user = config.twitter_credentials['gmail_user']
gmail_passwd = config.twitter_credentials['gmail_passwd']

def send_mail(msg):

	receiver = 'dave.splashpress@gmail.com'
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.ehlo()
	server.login(gmail_user, gmail_passwd)
	server.sendmail(gmail_user, receiver, msg)
	server.set_debuglevel(1)
	server.quit()


def oauth_authenticate():


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	print('Returning auth')
	return auth 


class MyStreamListener(tweepy.StreamListener):

	data_list=[]

	def __init__(self, save_file, start_time, time_limit):
		self.start_time = start_time
		self.time_limit = time_limit
		self.save_file = save_file
		super(MyStreamListener, self).__init__()

	def on_data(self, data):

		print(data)
		print('Getting data')
		if (time.time() - self.start_time) < self.time_limit:
			with open(self.save_file, 'a') as tf:
				tf.write(data)
				print('Saving data')
				return True

		else:


			print('Completed the twitter_data data stream')

			tweets_file = open(self.save_file, 'r')

			for line in tweets_file:
				try:
					tweet = json.loads(line)
					self.data_list.append(tweet)
				except:
					continue 

			print(len(self.data_list))

			MyStreamListener.parse_data(self.data_list)

			return False

	@staticmethod
	def parse_data(data_list):

		tweets_text = {}

		language = {}

		entities_data = {}

		tweets_text = list(map(lambda tweet: tweet['text'], data_list))

		print('.............')

		print(tweets_text) #prints out a list of all the text from the tweets

		print('.............')


		#Getthe dicts with the hashtags in
		entities_data = list(map(lambda tweet: tweet['entities']['hashtags'], data_list))
		print('Entities data: ')
		print(entities_data)
		print('.............')


		#get the users location if available
		location_data = list(map(lambda tweet: tweet['user']['location'], data_list))
		print('Location data: ')
		print(location_data)
		print('.............')

		user_names = []

		tweets = []

		for u in data_list:
			user_names.append(u['user']['name'])

		for tw in data_list:
			tweets.append(tw['text'])

		tweets_data = dict(zip(user_names, tweets))

		print('.............')

		print(tweets_data)

		print('.............')

		complete_msg = 'Twitter parse is complete' #placeholder msg for now a& for testing purposes


		send_mail(complete_msg)
		

	def on_error(self, status_code):
		if status_code == 420:
			return False





if __name__ == '__main__':


	start_time = time.time()
	
	l = MyStreamListener('twitter_data.txt', start_time, 20)
	auth = oauth_authenticate()
	stream = tweepy.Stream(auth, l)
	
	stream.filter(track=['pycon', 'python'])


	



