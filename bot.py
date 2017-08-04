import praw
import re
import time
from blacklist import *

try:
    from credentials import * # Python file containing USERNAME, PASSWORD, and USERAGENT config variables
except ImportError:
    print("Credentials file not available. You need to include a credentials.py file in the root directory. See README.")

# Configuration
LINK_PARSER = re.compile(r"\[([^\]]+)\]\(([^\)]+)\)", re.I) # Extract Markdown links
POST_LENGTH = 2 # Max length of link to expand

def get_links(message):
    matches = LINK_PARSER.findall(message.body)
    return (matches if matches else [])
def get_message(links):
    if len(links) == 1:
        text, url = links[0]
        return "[I've expanded that {} character link for you.]({})".format(len(text), url)
    else:
        m = "I've expanded some links for you."
        for text, url in links:
            length = len(text)
            qualifier = "character" if length == 1 else "characters"
            m += "\n\n**{}**: [Link expanded from {} {}]({})".format(text, length, qualifier, url)
        return m
def parse(message):
    links = get_links(message)
    messages = [link for text, url in links if len(text) <= POST_LENGTH] # List of links considered short
    return get_message(messages) if len(messages) > 0 else None

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
            except ConnectionResetError as error:
                print("Connection reset: ", error)
            except Exception as other_error:
                print(other_error)
main()
