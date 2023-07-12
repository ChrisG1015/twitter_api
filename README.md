# twitter_api
Basic Twitter API Script 
API Tokens used were for provided by a client. They had `ACADEMIC/RESEARCHER` tokens. This allows for 1 MILLION+ Tweets download. However Twitter API can only download `1000` tweets at a time. Trick here was to set up a cronjob to run this script every minute on the minuter for about 3 days. This cronjob and script were configured on an EC2 instance with decent size to store outputfiles.



# DATE PAIRS
Uses `date_pairs.json` to make API calls in between respective time. 
Example:
It will return all search-term-related-tweets between the times of `2:15 AND 2:17 on 28TH MARCH 2022`:
`{"date_since": "2022-03-28 02:15:00", "date_until": "2022-03-28 02:17:00"}`


# SEARCH TERMS
````
#searchterms = '(NBA Summer League) OR (Spurs) -is:retweet'
searchterms = '(Fenty) OR (fenty makeup)'
````