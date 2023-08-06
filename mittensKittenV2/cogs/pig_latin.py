import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Embed
import string

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
class pig_latin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="pig_latin",description="pig_latin")
    async def pig_latin(self,interaction: nextcord.Interaction, word: str):
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

def setup(bot):
    bot.add_cog(pig_latin(bot))




