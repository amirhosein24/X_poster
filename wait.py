import tweet
from time import sleep
from datetime import datetime
from tellbot import sendtoadmin

def tweetthething():
    tweet.posttweet()

def startwaiter():
    while True:
        now = datetime.now()

        if now.hour == 21 and now.minute == 0:
            tweetthething()
            sendtoadmin("sleeping for 24 h")
            sleep(86400) # wait a day
        else: # wait every 30 sec until its in a correct time loop
            sendtoadmin("sleeping for 30 s")
            sleep(30)

if __name__ == "__main__":
    startwaiter()