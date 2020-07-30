#! python3
import praw
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
reddit = config["Reddit"]
reddit = praw.Reddit(client_id = reddit["clientID"], \
                     client_secret = reddit["clientSecret"], \
                     user_agent = "LSF Scraper", \
                     username = reddit["redditAccountUsername"], \
                     password = reddit["redditAccountPassword"])
subreddit = reddit.subreddit("LivestreamFail")

def getDailyTopPosts(limit):
  postData = []
  for post in subreddit.top(time_filter="day", limit=limit):
    postData.append(post)
  return postData