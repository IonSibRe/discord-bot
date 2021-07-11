import discord
from discord.ext import commands
import requests
from dotenv import dotenv_values

# Variables
ENV_VARS = dotenv_values(".env")
DISCORD_TOKEN = ENV_VARS["TOKEN"]
API_URL = "https://yomomma-api.herokuapp.com"

helpMessage = """
!tvoje-mama - 1 mama joke
"""

# Config
client = commands.Bot(command_prefix="!")

# Functions
def getJoke():
    response = requests.get(f"{API_URL}/jokes")

    while True:
        joke = response.json()["joke"]

        if "poor" in joke.split() or "skinny" in joke.split():
            continue
        else:
            break

    return joke

# Events
@client.event
async def on_ready():
    print("Logged in as {0}".format(str(client.user).split("#")[0]))
    print("Started!")

# Commands
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)

@client.command(aliases=["tvoje-mama"])
async def tvoje_mama(ctx):
    joke = getJoke()
    await ctx.send(joke)

@client.command(aliases=["help"])
async def helpMsg(ctx):
    await ctx.send(helpMessage)

client.run(DISCORD_TOKEN)