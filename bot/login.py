import tweepy

consumer_key='cyxrVgAqqJAR5eRWYYMtYg'
consumer_secret='hY4SzjXiR7BMxWHzA9qiPxly4yKpB8rfZ5yoF6xbI'


access_token='798814963-DqTpdHxiL6XsIyxeAj7DNa9gk997qHKdsv5e7h74'
access_token_secret='aQ1sNUWlA0LaPYQXGDFrtY20DSFjC11KZhwHpj1zQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)




api = tweepy.API(auth)



#now using PostUpdate method of the api we can use to post an update on twitter account 

api.retweet("324208033041375232L")



    

