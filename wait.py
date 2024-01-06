import tweet
from time import sleep
from datetime import datetime
from tellbot import sendtoadmin

def tweetthething():
    tweet.posttweet()

def startwaiter():
    while True:
        now = datetime.now()

        if now.hour == 19 and now.minute == 49:
            tweetthething()
            sendtoadmin("sleeping for 24 h")
            sleep(86400) # wait a day
        else: # wait every 30 sec until its in a correct time loop
            sleep(30)

if __name__ == "__main__":
    startwaiter()