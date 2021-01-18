#!/usr/bin/env python

import requests
import logging
import json

logger = logging.getLogger(__name__)
GAMES_ENDPOINT="https://lichess.org/api/stream/games-by-users"

def stream(users):
    """
    Call endpoint to see if any games are running for two of the given usernames.
    """
    userpayload = ",".join(users)
    logger.info("Starting streaming games for %s", users)
    with requests.post(GAMES_ENDPOINT, data=userpayload, stream=True) as r:
        try:
            for line in r.iter_lines(chunk_size=1):
                if line:
                    logger.debug("Got line: %s", line)
                    yield line
        except Exception as cee:
            logger.exception("Error reading streams", cee)


def game_to_message(line):
    try:
        game = json.loads(line)
        player_white = game['players']['white']['userId']
        player_black=game['players']['black']['userId']
        # TODO Have a real Game object here
        game_ended = game["status"] != 20
        game_state = "ended" if game_ended else "started"
        url = "https://lichess.org/" + game["id"]
        # Hack to break cache in discord with the Embed
        if game_ended:
            url += "?1"
        return "Game {} between {} and {}, URL is: {}".format(game_state,
                                                              player_white,
                                                              player_black,
                                                              url)
    except Exception as e:
        logger.exception("Couldn't decode %s", line, e)


