import tweepy
api_key = "s6jlXimmDZ4AHproJDVahhVxv"
api_secret = "z2rwxo6zUoTpEC2GtLZp7EblE7SqMSqiFyjIQUxeWCJ2QnhQwO"
access_token = "990323260901347329-UpYUQFZLcQDdsBSUJpxJkrDsl04LVPR"
access_token_secret = "d6pd4Mc8jvLA2lJb8zhKY0jVTqDwx38B3HJC5SEd1P8dJ"

# oAuth is used for authentication purpose
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

#show friendships
def are_frnds():
    a=api.show_friendship(source_screen_name="BarackObama",target_screen_name="realDonaldTrump")
    print(a)
are_frnds()