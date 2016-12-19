# LinkExpanderBot
[![License](https://img.shields.io/:license-mit-blue.svg)](https://astrocb.mit-license.org)

## About

LinkExpanderBot is a [Reddit](https://reddit.com/) bot designed to help mobile users by expanding comment links that are too short to be easily clicked. It replies to comments containing any number of links that meet the configured length requirement (1-2 characters by default). Built using [PRAW](http://praw.readthedocs.io/en/stable/) and Python 3.

## Configuration

If you'd like to fork/clone this bot, you'll have to set up a configuration file with the requisite information for accessing read/write features of the API.

You'll need to create a Reddit account for your bot (or simply use your existing account). Once you have the username/password for the account you'd like the bot to post under, create a file in the root directory called `credentials.py`.

It should contain 3 variables: `USERNAME`, `PASSWORD`, and `USERAGENT`, an identifier required to access the Reddit API. This can be anything you like, but make sure it's unique. It's also a good idea to include a version in the user agent so that it can be easily changed if it gets blocked for some reason (not that you would spam the Reddit API or anything...).

Example `credentials.py` file:

```py
USERNAME="mybot123"
PASSWORD="mypass123"
USERAGENT="MyBot 1.0.0"
```

Then, just run `bot.py` through a Python 3 interpreter and you're good to go.

## Blacklist
Not everyone is a fan of our dear LinkExpanderBot. As a result, it has been banned from a few subreddits and a few users have requested that their comments not be subject to its scrutiny. As a result, I've included a blacklist to prevent it from posting in certain subs and responding to certain users.

The files are pretty self-explanatory; each line of `sub_blacklist.txt` and `user_blacklist.txt` represent an individual blacklisted sub and user respectively. Add to the blacklist as necessary by simply adding lines to these files. The bot will recompile its blacklist database each time you run it, and it will not post in blacklisted subs or respond to blacklisted users.

I've preloaded the sub blacklist with the subs that [the official LinkExpanderBot](https://reddit.com/user/LinkExpanderBot) is currently banned from and the user blacklist with a few bots that tend to have short links in their posts (we don't want to start any bot wars here).

If you're using this bot for some other purpose where you think it would be welcome in these communities and/or by these users, feel free to purge the lists and start anew.

The code could also be easily modified to use a whitelist if that's more of what you're looking for.
