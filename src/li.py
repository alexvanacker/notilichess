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


def game_to_message(line):
    game = json.loads(line)
    player_white = game['players']['white']['userId']
    player_black=game['players']['black']['userId']
    # TODO Have a real Game object here
    game_state = "started" if game["status"] == 20 else "ended"
    url = "https://lichess.org/" + game["id"]
    return "Game {} between {} and {}, URL is: {}".format(game_state,
                                                          player_white,
                                                          player_black,
                                                          url)

