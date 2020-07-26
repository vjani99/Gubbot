import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Techlipse!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    gameOfThrones_quotes = [
        'Winter is coming ❄️',
        'Power is power 💪🏽',
        'When you play a game of thrones, you win or you die ⚔️',
        'You know nothing Jon Snow 🧔🏻',
        'Everything before the word "but" is horseshit 💩',
        'Chaos is a ladder 💡',
    ]

    if message.content == 'GoT':
        response = random.choice(gameOfThrones_quotes)
        await message.channel.send(response)

    if message.content.lower() == 'valar morghulis':
        await message.channel.send('Valar Dohaeris')

client.run(TOKEN)
