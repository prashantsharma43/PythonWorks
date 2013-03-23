import twitter

import random as rm

a="This the second day. Ok"

api=twitter.Api(consumer_key='cyxrVgAqqJAR5eRWYYMtYg',consumer_secret='hY4SzjXiR7BMxWHzA9qiPxly4yKpB8rfZ5yoF6xbI',access_token_key='798814963-DqTpdHxiL6XsIyxeAj7DNa9gk997qHKdsv5e7h74',access_token_secret='aQ1sNUWlA0LaPYQXGDFrtY20DSFjC11KZhwHpj1zQ') 

#now using PostUpdate method of the api we can use to post an update on twitter account 

status=api.PostUpdate(a)
print status.text 
