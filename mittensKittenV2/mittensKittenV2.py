# This example requires the 'message_content' intent.


import os 
from dotenv import load_dotenv
load_dotenv()
import nextcord
import string

intents = nextcord.Intents.default().all()

intents.message_content=True
from nextcord.ext import commands

import re
import random

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
    if message.content.startswith('nani'.lower()):
        channel = message.channel
        await channel.send('UwU')
    if message.content.startswith('test'.lower()):
        channel = message.channel
        await channel.send('ed')


#only use lowercase for names
@bot.slash_command(description="ping" )
async def ping(interaction: nextcord.Interaction):
    await interaction.send("pong")


@bot.slash_command(name="dice_roll",description="dice_roll")
async def dice_roll(interaction: nextcord.Interaction, num:int):
    result=0;
    if(re.match("^\\d+$",str(num))):
        if(num<2 or num>100):
            await interaction.response.send_message(f"{num} is out of range. please choose a value between 2 and 100")
        result=random.randrange(1,num)
        await interaction.response.send_message(f"Rolling a D{num}\nYou rolled {result}")
    else:
        return   

##Helper functions for pig latin
##########################################################################################
vowels = ["a","e","i","o","u","y"]
def vowelChecker(arg):

    for y in range(len(vowels)):
        if arg[0].lower()==vowels[y]:
            return True

def VowelModifier(arg):
    return (arg+"yay").lower()

def consonantModifier(arg):
    count=0
    for y in range(len(arg)):
        if not vowelChecker(arg[y]):
            count=count+1
        else:
            break
    if(arg[1].lower()=="y"):
        count=2
    return (arg[count:len(arg)]+arg[0:count]+"ay").lower()



@bot.slash_command(name="pig_latin",description="pig_latin")
async def pig_latin(interaction: nextcord.Interaction, word: str):
    #await interaction.response.send_message(f"You said: {arg[0:len(arg)-1]}")
    arg=word.split()
    finalWord=""
    for x in range(len(arg)):
        arg[x]=arg[x].strip(string.punctuation)

        if(len(arg[x])>1):
            if vowelChecker(arg[x]):
                finalWord=finalWord+VowelModifier(arg[x])+" "
                
            else:
                #consonantModifier(arg)
                finalWord=finalWord+consonantModifier(arg[x])+" "
        elif(len(arg[x])==1):
            finalWord=finalWord+(arg[x].upper())+" "
        else:
            return
    await interaction.response.send_message(f"Original sentence:\t{word}\nPig latin:\t{finalWord}")
#################################################################################################
 
bot.run(BotToken)