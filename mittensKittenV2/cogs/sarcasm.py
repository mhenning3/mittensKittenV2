
import os
import sys
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Embed
import re

class sarcasm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="sarcasm",description="ReTuRnS tHiS tExT")
    async def sarcasmCommand (self,interaction: nextcord.Interaction, words:str):
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


def setup(bot):
    bot.add_cog(sarcasm(bot))



