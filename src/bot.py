import discord
from dotenv import load_dotenv
import json
import li
import os


description = ''' A bot that notifies when players are playing one another.'''
load_dotenv()
TOKEN_KEY="BOT_TOKEN"
LICHESS_URL="https://lichess.org/"


chess_channel_id = 774153683944210434
# TODO load this from a data store and add CRUD to edit that list
users=["Le_Scratch","justmaker","kazeriahm","Khrok","paupausco","rio77"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channel = client.get_channel(chess_channel_id)

        for line in li.stream(users):
            message = li.game_to_message(line)
            if message:
                print('Sending message: {}'.format(message))
                await channel.send(message)


client = MyClient()
if not os.getenv(TOKEN_KEY):
    print("ERROR loading bot token")
    exit(1)
token = os.getenv(TOKEN_KEY)

client.run(token)
