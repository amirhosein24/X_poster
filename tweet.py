import creds
from requests_oauthlib import OAuth1Session


consumer_key = creds.apikey
consumer_secret = creds.apikeysecret

proxies = {'http': 'socks5://localhost:2080', 'https': 'socks5://localhost:2080'}
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"

oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url, proxies=proxies)
resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)


import tellbot
import time

verifier = tellbot.getpin(authorization_url)

while verifier is None:
    time.sleep(2)

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier)

access_token_url = "https://api.twitter.com/oauth/access_token"
oauth_tokens = oauth.fetch_access_token(access_token_url, proxies=proxies)
access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret)


def posttweet():
    response = oauth.post("https://api.twitter.com/2/tweets", json={"text": creds.tweet}, proxies=proxies)

    if response.status_code != 201:
        tellbot.sendtoadmin(f"error 201\n{response.json()}")

    tellbot.sendtoadmin(str(response.json()))