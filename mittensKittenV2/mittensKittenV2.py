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



###############################
#Dice helper function
 
@bot.slash_command(name="dice_roll",description="Rolls a specified number of dice", )
async def dice_roll(interaction: nextcord.Interaction, d: int, amount: int):
    result=f"Rolling {amount} D{d}\nRolls:\n"
    nums=0
    total=0
    if(amount<1):
        await interaction.response.send_message("Roll at least 1 die smartass")
    elif(amount>100):
        await interaction.response.send_message("This isn't a bag of holding. I can only go up to 100")
    else:
        if(re.match("^\\d+$",str(d))):
            if(d<2 or d>100):
                await interaction.response.send_message(f"{d} is out of range. please choose a value between 2 and 100")
            for x in range(amount):
                nums=random.randrange(1,d)
                result=result+f"{nums}\t"
                total=total+nums
            result=result+f"\nTotal {total}"
            await interaction.response.send_message(result)
            return;
        else:
            return  




@bot.slash_command(name="sarcasm",description="sarcasm")
async def sarcasm (interaction: nextcord.Interaction, words:str):
    track=1;
    newWord=""
    for x in range(len(words)):
        if(words[x]==" "):
            newWord=newWord+" "
        elif(re.match("[a-zA-Z]",str(words[x]))):
            if(track%2==0):
                newWord=newWord+words[x].lower()
            else:
                newWord=newWord+words[x].upper()
            track+=1
        else:
            newWord=newWord+words[x]
    await interaction.response.send_message(f"{newWord}")
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