import tweepy
import os
import csv
from pathlib import Path
from dotenv import load_dotenv

root_dir = Path(os.path.abspath("__file__")).parent
dataset_dir = root_dir / "data"

load_dotenv()

# Go to https://developer.twitter.com/en/apps to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://developer.twitter.com/en/docs/basics/authentication/overview/oauth
# for more information on Twitter's OAuth implementation.

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.getenv("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

keywords = [
    "COVID-19",
    "COVID19",
    "covid-19",
    "covid19",
    "coronavirus",
]

date_since = "2019-12-31"

tweets = tweepy.Cursor(
    api.search,
    q=" OR ".join(keywords),
    lang="en",
    since=date_since
).items()

f = open(dataset_dir / "test.csv", "a")
count = 0

for tweet in tweets:
    f = open(dataset_dir / "test.csv", "a")
    csv_file = csv.writer(f)
    l = list(map(lambda x: x["text"],tweet.entities["hashtags"]))
    if l:
        count += 1
        csv_file.writerow(l)
        print(f"\rcount: {count} ", end="")
    f.close()

f.close()