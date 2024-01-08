import tweet
from time import sleep

from tellbot import sendtoadmin

def tweetthething():
    tweet.posttweet()

def startwaiter():
    while True:
        tweetthething()
        sendtoadmin("sleeping for 5 h")
        sleep(18000) # wait a day

if __name__ == "__main__":
    startwaiter()