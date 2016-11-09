import praw
import re
from redditreplier import Replier
from credentials import *

class Parser:
    LINK_PARSER = re.compile(r"\[([^\]]+)\]\(([^\)]+)\)", re.I) # Extract Markdown links
    def parse(self, message):
        links = Parser.get_links(message)
        for link in links:
            text = link[0]
            url = link[1]
            if len(text) < 3: # Considered short link
                print(Parser.get_message(url, len(text)))
                # return True, Parser.get_message(url)
        return False, ''
    def get_links(message):
        matches = Parser.LINK_PARSER.findall(message.body)
        return (matches if matches else [])
    def get_message(url, length):
        return """
        [I've expanded that {1} character link for you.]({0})
        """.format(url, length)

bot = Replier(Parser(), USERNAME, PASSWORD, user_agent="LinkExpander 1.0")
bot.start()
