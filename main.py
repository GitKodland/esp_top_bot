from settings import settings
import discord
# import * - is a quick way to import all files in the library
from bot_logic import *

# The intents variable stores the bot's priviliges
intents = discord.Intents.default()
# Enabling the message-reading privelege
intents.message_content = True
# Creating a bot in the client variable and transferring it the priveleges
client = discord.Client(intents=intents)


# Once the bot is ready, it will print its name!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# When the bot receives a message, it will send messages in the same channel!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hi! I am a bot!')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Can't process this command, sorry!")

client.run(settings["TOKEN"])
