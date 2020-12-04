#!/usr/bin/env python

import requests
import json


GAMES_ENDPOINT="https://lichess.org/api/stream/games-by-users"

def stream(users):
    """
    Call endpoint to see if any games are running for two of the given usernames.
    """
    userpayload = ",".join(users)
    print("Starting streaming games for {}".format(users))
    r = requests.post(GAMES_ENDPOINT, data=userpayload, stream=True)

    for line in r.iter_lines(chunk_size=1):
        if line:
            print(line)
            yield line
