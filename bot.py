import discord
from discord.ext import commands

from creds import token
import logging

logging.basicConfig(filename="bot.log", level=logging.INFO)
LOG = logging.getLogger()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    LOG.info('Bot is starting...')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    channel = msg.channel
    await channel.send(msg.content)

client.run(token)