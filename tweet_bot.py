import requests
import os
import pandas as pd
import json


# Add bearer token, twitter id, and csv path to your environment variables as
# BEARER_TOKEN, TWITTER_ID, and TWEET_FILE

bearer_token = os.environ.get("BEARER_TOKEN")
twitter_id = os.environ.get("TWITTER_ID")
tweet_location = os.environ.get("TWEET_FILE")
payload_url = os.environ.get("WEBHOOK")

# Change the username in this URL to the user who's tweets you want to push
tweet_base_uri = "https://www.twitter.com/bertthegorilla/status/"


def read_tweet() -> str:
    """
    Grabs stored tweet id from csv file and returns it
    """
    tweet = pd.read_csv(tweet_location)['new_tweet'][0]
    return tweet


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = "Bearer {}".format(bearer_token)
    r.headers["User-Agent"] = "Bert's Twitter Bot for Discord"
    return r


def check_new() -> list:
    """
    Checks if latest tweet id matches stored tweet id and returns a list with an id and boolean
    """
    latest_tweet = str(read_tweet())
    url = "https://api.twitter.com/2/users/{}/tweets".format(twitter_id)
    parameters = {"tweet.fields": "created_at"}
    req = requests.get(url, params=parameters, auth=bearer_oauth).json()
    new_tweet = req['meta']['newest_id']
    if latest_tweet != new_tweet:
        return [new_tweet, True]
    else:
        return [latest_tweet, False]


def main():
    """
    overwrites .csv file with tweet id and pushes the tweet to webhook if it is declared new
    """
    print("Checking for new Tweets...")
    tweet_id = check_new()
    data = dict(new_tweet=[tweet_id[0]])
    payload = json.dumps(dict(content=tweet_base_uri+tweet_id[0]))
    pd.DataFrame(data=data).to_csv(tweet_location, encoding="utf-8")
    if tweet_id[1] is True:
        requests.post(payload_url, data=payload,
                      headers={'Content-Type': 'application/json'})


if __name__ == "__main__":
    main()
