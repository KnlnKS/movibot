import os
import praw
import re


def search_comment_for_title(text):
    for x in range(len(text)):
        if text[x-1:x+7] == "!movibot":
            txt1=(text[x+8:].split("{",1))
            return ((txt1[-1].split("}",1))[0])



