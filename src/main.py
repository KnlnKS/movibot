import os
import praw
import re
import src.comment_builder
import src.comment_scrapper


r=praw.Reddit("movibot")
subreddit=r.subreddit("pythonforengineers")

for comment in subreddit.stream.comments():
    if re.search("!movibot", comment.body, re.IGNORECASE):
            title=src.comment_scrapper.search_comment_for_title(comment.body)
            movie = src.comment_builder.search_movie(title)
            print(movie)
            reply = src.comment_builder.build_comment(movie)
            comment.reply(reply)
            print("Commented: ")
            print(reply)
            print("--------------------------------------------------------")