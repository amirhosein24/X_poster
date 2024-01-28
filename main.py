import tweet
from time import sleep
from datetime import datetime

# importing tellbot isnt needed, its imported in tweet
# from tellbot import sendtoadmin

def startwaiter():
    while True:
        now = datetime.now()

        try:
            if now.hour == 21 and now.minute == 0:
                tweet.posttweet()
                tweet.tellbot.sendtoadmin("sleeping for 24 h")
                sleep(86400 - 60) # wait 1 min less than 24 h
            else: # wait every 10 sec until its in a correct time loop
                sleep(5)
        except Exception as e:
            tweet.tellbot.sendtoadmin(f"error main loop:\n{e}")

if __name__ == "__main__":
    startwaiter()