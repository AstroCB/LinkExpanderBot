# TODO: allow users to modify the blacklist by replying to the bot

def _parse_into_list(f):
    L = []
    with open(f) as _file:
        L = _file.read().split("\n")[:-1] # Slice removes last (blank) line
    return L

# Exposed data
BLACKLISTED_USERS = _parse_into_list("user_blacklist.txt")
BLACKLISTED_SUBS = _parse_into_list("sub_blacklist.txt")
