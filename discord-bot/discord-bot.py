import discord
import os
import asyncio
from dotenv import load_dotenv

APPLICATION_ID = "1109692575809556482"
PUBLIC_KEY = "b653b3c92769c40dce6551c50a09e43fb9bc64e6213f571f3000eba894687f2b"
CHANNEL_ID = 1109712323066728459

load_dotenv()  # Load environment variables from .env file
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')  # Retrieve the token from the environment

client = discord.Client(command_prefix="*", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # Fetch the target channel
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send('/imagine test')
    else:
        print(f'Channel with ID {CHANNEL_ID} not found.')

    # Close the connection
    await client.close()

# Run the client
client.run(DISCORD_TOKEN)