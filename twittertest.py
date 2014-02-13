import twitter
api = twiiter.Api()
statuses = api.GetPublicTimeline()
print [s.text for s in statuses]
