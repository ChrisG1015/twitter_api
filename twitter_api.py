from datetime import datetime
from datetime import timedelta
import tweepy
import pandas as pd
import time
import os
import subprocess
import json


#date_since = datetime(2022,3,27,17,0,0)
#date_until = datetime(2022,3,27,17,1,0)
api_key = ''
api_key_secret = ''
bearer_token = ''
access_token_secret = ''
access_token = ''
client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)
api = tweepy.API(authenticator, wait_on_rate_limit=True)
tweet_mode = 'extended'
#searchterms = '(NBA Summer League) OR (Spurs) -is:retweet'
searchterms = '(Fenty) OR (fenty makeup)'
language = 'en'
count = 100





date_list = []

with open('date_pairs.json') as json_file:
    date_pairs_json = json.load(json_file)


# GET LAST date_since_obj AND date_until_obj FROM date_pairs.json FILE 
date_since_obj = datetime.strptime(date_pairs_json['date_since'], '%Y-%m-%d %H:%M:%S')
date_until_obj = datetime.strptime(date_pairs_json['date_until'], '%Y-%m-%d %H:%M:%S')

# ADD 1 MINUTE TO EACH
date_since = date_since_obj + timedelta(minutes=+2)
date_until = date_until_obj + timedelta(minutes=+2)

# PERFORM TWEEPY LOGIC
response = client.search_all_tweets(query=searchterms, start_time=date_since, end_time=date_until, max_results=count, tweet_fields=['author_id', 'lang', 'created_at'])
time.sleep(5)
tweets = response.data

# SAVE TWEETS TO DATAFRAME
sentiments_df = pd.DataFrame(tweets)
sentiments_df = sentiments_df[sentiments_df['lang'] == 'en']

current_time = datetime.now().strftime('%H:%M:%S')
print("DATAFRAME CREATED")

sentiments_df.to_csv('{}-willsmith_slap_sentiment_analysis_data.csv'.format(current_time)) 


# COLLECT DATE PAIRS
date_pairs = [date_since, date_until]


# SAVE DATE PAIRS TO LIST
date_list.append(date_pairs)
# SAVE LAST DATE PAIR TO DICTIONARY
date_pairs_list = [str(i) for i in date_list[-1]]
date_pairs = {'date_since': date_pairs_list[0],
              'date_until': date_pairs_list[1]}


# SAVE THE LAST DATE PAIR AS NEW date_since_obj AND date_until_obJ IN JSON FILE
with open('date_pairs.json', 'w') as outfile:
    json.dump(date_pairs, outfile)


print("NEW DATE PAIRS: {}".format(date_pairs))