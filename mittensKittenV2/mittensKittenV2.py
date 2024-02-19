# This example requires the 'message_content' intent.


import os 
from dotenv import load_dotenv
load_dotenv()
import nextcord
import random


intents = nextcord.Intents.default().all()

intents.message_content=True
from nextcord.ext import commands


AppId=os.getenv("APPID")
GuildId=986407383611867147
BotToken=os.getenv("TOKEN")
CredToken=os.getenv("CREDS")



class kitten(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='+', help_command=None, intents=intents)

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.load_extension(f"cogs.{filename[:-3]}")
        self.super = super()

bot = kitten()




@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}, sup bitches')

    #await message.channel.send('We have logged in as {bot.user}, sup bitches')

with open('insultList.txt', 'r') as file:
    data = file.read().splitlines()
@bot.event
async def on_message(message):
    #print(f'Message from {message.author}: {message.content}')
    channel = message.channel
    if message.content.startswith('nani'.lower()):
        await channel.send('UwU')
    if message.content.startswith('test'.lower()):
        await channel.send('ed')
    num=random.randint(1,200)
    #data['insults'] is the array format
    if(num==1):
        num2=random.randint(0,len(data)-1)
        await channel.send(data[num2])
    


#only use lowercase for names
@bot.slash_command(description="ping" )
async def ping(interaction: nextcord.Interaction):
    await interaction.send("pong")


 
bot.run(BotToken)