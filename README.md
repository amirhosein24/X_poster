# X poster

This repository contains a collection of Python scripts for automate posting on X (tweeter).

## Files

- `main.py` - Imports and runs the wait script  
- `wait.py` - Schedules sending automated tweets daily using the Twitter API
- `tweet.py` - Handles posting tweets via the Twitter OAuth1 API
- `tellbot.py` - Telegram bot that captures user input for Twitter OAuth verification PIN

## Overview

The scripts work together to send an automated tweet daily at 9 PM:

- `main.py` - Starts up the waiter script
- `wait.py` - Sleeps and checks current time, runs tweet script at 9 PM
- `tweet.py` - Posts a tweet via OAuth1 session
- `tellbot.py` - Telegram bot listens for PIN input to authorize tweet.py
- `creds.json` - for storing Credentials

## json format for Credentials

{
    "apikey" : "tweeter-api-token",
    "apikeysecret" : "tweeter-apisecret-token",
    "telbottoken" : telegrambot-apikey",
    "admin" : "your-telegram-chatid",
    "tweet" : "text-to-post"
}
