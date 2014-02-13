import twitter

client = twitter.Api()

latest_posts = client.GetUserTimeline("_moshpit")
print [s.text for s in latest_posts]
