import json
import tweepy


with open(__file__[:-6]+"creds.json") as file:
    data = json.load(file)

consumer_key = data["apikey" ]
print(consumer_key)
consumer_secret = data["apikeysecret"]
access_token = data["accesstoken"]
access_token_secret = data["accesstokensecret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet_text = "Hello, Twitter!"
try:
    api.update_status(tweet_text)

    print("Tweet posted successfully!")

except Exception as e:
    print(e)



# client = tweepy.Client(
#     consumer_key=consumer_key,
#     consumer_secret=consumer_secret,
#     access_token=access_token,
#     access_token_secret=access_token_secret
# )

# # Post Tweet
# message = " MESSAGE "
# client.create_tweet(text=message)
# print("Tweeted!")