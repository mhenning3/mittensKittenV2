# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print(f'We have logged in as {client.user}, sup bitches')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ping'):
        await message.channel.send('pong')
    if message.content.startswith('$nan'):
        await message.channel.send('UwU')

 
client.run('TOKEN')