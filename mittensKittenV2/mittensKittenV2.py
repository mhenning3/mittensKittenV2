# This example requires the 'message_content' intent.


import os 
from dotenv import load_dotenv
load_dotenv()
import nextcord


intents = nextcord.Intents.default().all()

intents.message_content=True
from nextcord.ext import commands



AppId=os.getenv("APPID")
GuildId=986407383611867147
BotToken=os.getenv("TOKEN")
CredToken=os.getenv("CREDS")


bot = commands.Bot( intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}, sup bitches')
    #await message.channel.send('We have logged in as {bot.user}, sup bitches')


@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.content.startswith('nani'):
        channel = message.channel
        await channel.send('UwU')



@bot.slash_command(description="ping", guild_ids=[GuildId])
async def ping(interaction: nextcord.Interaction):
    await interaction.send("pong")

@bot.slash_command(description="dice roll", guild_ids=[GuildId])
async def ping(interaction: nextcord.Interaction):
    await interaction.send("dice")




 
bot.run(BotToken)