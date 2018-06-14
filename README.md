# TwitterStreamParse

Uses Tweepy API to pull data from Twitter for specific keywords for a set period of time and downloads data to a text file.

Install Tweepy with pip

pip install tweepy
Signup and create a Twitter application with API access at Twitter.com to get required keys:

https://apps.twitter.com

Save your Twitter apps access token & secret as well as your consumer key & secret and also Gmail username and password to a file config.py using this format:

twitter_credentials = dict(

    ACCESS_TOKEN = '',
    ACCESS_SECRET = '',
    CONSUMER_KEY = '',
    CONSUMER_SECRET = '',
    gmail_user = '',
    gmail_passwd = ''
)
