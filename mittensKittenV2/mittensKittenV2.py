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


@bot.event
async def on_message(message):
    #print(f'Message from {message.author}: {message.content}')
    if message.content.startswith('nani'):
        channel = message.channel
        await channel.send('UwU')
    if message.content.startswith('test'):
        channel = message.channel
        await channel.send('ed')


#only use lowercase for names
@bot.slash_command(description="ping" )
async def ping(interaction: nextcord.Interaction):
    await interaction.send("pong")


 
bot.run(BotToken)