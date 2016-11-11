import praw
import re
import time
from blacklist import *

try:
    from credentials import * # Python file containing USERNAME, PASSWORD, and USERAGENT config variables
except ImportError:
    print("Credentials file not available. You need to include a credentials.py file in the root directory. See README.")

LINK_PARSER = re.compile(r"\[([^\]]+)\]\(([^\)]+)\)", re.I) # Extract Markdown links
POST_LENGTH = 3 # Max length of expansion

def get_links(message):
    matches = LINK_PARSER.findall(message.body)
    return (matches if matches else [])
def get_message(links):
    if len(links) == 1:
        l = links[0]
        return "[I've expanded that {} character link for you.]({})".format(len(l[0]), l[1])
    else:
        m = "I've expanded some links for you."
        for l in links:
            length = len(l[0])
            qualifier = "character" if length == 1 else "characters"
            m += "\n\n**{}**: [Link expanded from {} {}]({})".format(l[0], length, qualifier, l[1])
        return m
def parse(message):
    messages = []
    links = get_links(message)
    for link in links:
        text = link[0]
        url = link[1]
        if len(text) < POST_LENGTH: # Considered short link
            messages.append(link)
    if len(messages) > 0:
        return get_message(messages)
    return None

def main():
    r = praw.Reddit(USERAGENT)
    r.login(USERNAME, PASSWORD, disable_warning=True)
    for comment in praw.helpers.comment_stream(r, 'all'):
        resp = parse(comment)
        if resp and not (str(comment.author) in BLACKLISTED_USERS or str(comment.submission.subreddit) in BLACKLISTED_SUBS):
            try:
                print(resp)
                comment.reply(resp.lstrip())
            except praw.errors.RateLimitExceeded as error:
                # Rate limit error
                print("Sleeping for {} seconds".format(error.sleep_time))
                time.sleep(error.sleep_time) # Delay to prevent ratelimiting
            except ConnectionError as error:
                print("HTTP connection error: ", error)
            except Exception as other_error:
                print(other_error)
main()
