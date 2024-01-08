from json import load
from requests_oauthlib import OAuth1Session
import gpt

with open("creds.json", encoding='utf-8') as file:
    data = load(file)

consumer_key = data["apikey" ]
consumer_secret = data["apikeysecret"]

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

# verifier=13513
verifier = tellbot.getpin(authorization_url)

while verifier is None:
    time.sleep(2)


access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier
)
oauth_tokens = oauth.fetch_access_token(access_token_url, proxies=proxies)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret
)

def posttweet():
    response = oauth.post("https://api.twitter.com/2/tweets", json={"text": gpt.ask_gpt("tell me a crazy, insane fact that not popular, make it short and one sentence and dont write anything else, start you sentenc with: میدونستی ...")}, proxies=proxies)

    if response.status_code != 201:
        tellbot.sendtoadmin("error 201")
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))

    tellbot.sendtoadmin(str(response.json()))