import os
import pandas as pd
import sys

keyword = sys.argv[1] + ' ' + sys.argv[2]

path = "/kaggle/working/TweetCrawler/raw_data/democrat"
# Check whether the path exists or not
if not os.path.exists(path):
   os.makedirs(path)

tweet_count = int(1e7)
since_date = sys.argv[3]   
until_date = sys.argv[4] #"2022-11-09"

print("Starting process to scrape tweets containing " + keyword + " ...")
filename = keyword.replace(' ', '')
os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}"> /kaggle/working/TweetCrawler/raw_data/democrat/democrat_{}.json'.format(tweet_count, since_date, keyword, until_date, filename))
print("Scraping tweets containing " + keyword + ": DONE")
