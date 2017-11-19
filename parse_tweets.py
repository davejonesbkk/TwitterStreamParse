#Script to parse Twitter json data from file to get usernames and tweets text

import json

import pandas as pd

file = 'pycontwitter_data.txt'

data = []

tweets_file = open(file, 'r')

for line in tweets_file:
	try:
		tweet = json.loads(line)
		data.append(tweet)
	except:
		continue 

print(len(data))


tweets_text = {}

language = {}

entities_data = {}


tweets_text = list(map(lambda tweet: tweet['text'], data))

#print(tweets_text)#prints out a list of all the text from the tweets

#this gets the dicts with the hashtags in
entities_data = list(map(lambda tweet: tweet['entities']['hashtags'], data))

#print(entities_data)#prints the hashtags used and their indices

#get the users location if available
location_data = map(lambda tweet: tweet['user']['location'], data)

#print(location_data)

user_names = []

tweets = []


for u in data:
	user_names.append(u['user']['name'])
	
for d in data:
	tweets.append(d['text'])

#print('Printing usernames')
#print(user_names)

#print('Printing Tweets text')
#print tweets

tweets_data = dict(zip(user_names, tweets))

print(tweets_data)




	
	








