import discord
from dotenv import load_dotenv
import json
import li
import os
import logging


description = ''' A bot that notifies when players are playing one another.'''
load_dotenv()
TOKEN_KEY="BOT_TOKEN"
CHESS_CHANNEL_ID_KEY="CHESS_CHANNEL_ID"
LICHESS_URL="https://lichess.org/"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
logger = logging.getLogger(__name__)
logging.getLogger('discord.gateway').disabled = True


chess_channel_id = int(os.getenv(CHESS_CHANNEL_ID_KEY))
if not chess_channel_id:
    logger.error("Could not read %s from .env file", CHESS_CHANNEL_ID_KEY)
logger.info("Channel ID on which we'll notify: %s", chess_channel_id)

# TODO load this from a data store and add CRUD to edit that list
users=["Le_Scratch","justmaker","kazeriahm","Khrok","paupausco","rio77","tbwtbw"]

class MyClient(discord.Client):
    async def on_ready(self):
        logger.info('Logged on as %s', self.user)
        channel = client.get_channel(chess_channel_id)
        if not channel:
            logger.error("Could not access channel %s", chess_channel_id)


        logger.info('Will notify on %s', channel.name)
        for line in li.stream(users):
            message = li.game_to_message(line)
            if message:
                logger.info('Sending message: %s', message)
                await channel.send(message)


client = MyClient()
token = os.getenv(TOKEN_KEY)
if not token:
    logger.error("Could not load %s from .env file", TOKEN_KEY)
    exit(1)

client.run(token)
