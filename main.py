import discord
import requests
from dotenv import dotenv_values

ENV_VARS = dotenv_values(".env")
DISCORD_TOKEN = ENV_VARS["TOKEN"]
API_URL = "https://yomomma-api.herokuapp.com"

helpMessage = """
!tvoje-mama - 1 mama joke
"""

client = discord.Client()

def getJoke():
    response = requests.get(f"{API_URL}/jokes")

    while True:
        joke = response.json()["joke"]

        if "poor" in joke.split() or "skinny" in joke.split():
            continue
        else:
            break

    return joke

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    # Log
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    # Return for messages send by the bot
    if (message.author == client.user):
        return

    if message.channel.name == 'bot':
        # Help
        if user_message.lower() == "!help":
            await message.channel.send(helpMessage)
            return

        # Joke  
        if user_message.lower() == "!tvoje-mama":
            joke = getJoke()
            await message.channel.send(joke)
            return

        # Fiola
        if username == "HopperW12" and user_message:
            joke = getJoke()
            await message.channel.send(f"Tvoje máma Fiolo :)\n{joke}")
            return

        # Zugabuk
        if username == "ZugabukCZ":
            joke = getJoke()
            await message.channel.send(f"Tvoje máma Zugabuku :)\n{joke}")
            return
            

client.run(DISCORD_TOKEN)