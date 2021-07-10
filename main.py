import discord
import random
from dotenv import dotenv_values

envVars = dotenv_values(".env")
apiToken = envVars["TOKEN"]

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if (message.author == client.user):
        return

    if message.channel.name == 'bot':
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"Goodbye {username}")
            return
        elif user_message.lower() == "!random":
            response = f"This is your random number: {random.randrange(1000000)}"
            await message.channel.send(response)
            return
    
    if user_message.lower() == "!anywhere":
        await message.channel.send("This can be send anywhere")
        return

client.run(apiToken)