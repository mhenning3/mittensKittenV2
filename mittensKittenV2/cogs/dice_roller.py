import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Embed
import re
import random


#Dice helper function
def listSplit(nums):
    listNums=nums.split("+")
    for x in range(len(listNums)):
        listNums[x]=listNums[x].strip()
        listNums[x]=int(listNums[x])
    return listNums

class dice_roller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="dice_roll",description="Rolls a specified number of dice", )
    async def dice_roll(self,interaction: nextcord.Interaction, d: str= SlashOption(description="number of sides (x+y for multiple types)"), amount: str= SlashOption(description="number of dice")):
        embedTitle=f"Rolling "
        result=""
        nums=0
        total=0
        numlist=""
        reject=False
        triggernumD=0

        if(re.match("[0-9,+]",d) and re.match("[0-9,+]",amount)):
            d=listSplit(d)
            amount=listSplit(amount)
            if(len(d)!=len(amount)):
                difference=len(d)-len(amount)
                if(difference>0):
                    await interaction.response.send_message(f"Length mismatch\n{difference} more dice types than amount specified")
                else:
                    await interaction.response.send_message(f"Length mismatch\n{abs(difference)} more dice specified than dice types")
                return
            else:
                for x in range(len(d)):
                    if(amount[x]<1):
                        await interaction.response.send_message("Roll at least 1 die smartass")
                        return
                    elif(amount[x]>100):
                        await interaction.response.send_message("This isn't a bag of holding. I can only go up to 100")
                        return
                    if(d[x]<2 or d[x]>100):
                        reject=True
                        triggernumD=x
                        return
                    for y in range(amount[x]):
                        nums=random.randrange(1,d[x]+1)
                        total=total+nums
                        if y==0:
                            numlist=numlist+f"\n\tD{d[x]}:\t"
                        numlist=numlist+f"{nums}\t"

                    if(x<len(d)-1 and len(d)>1):
                        embedTitle=embedTitle+f"{amount[x]} D{d[x]}, "
                     
                      
                embedTitle=embedTitle+f" {amount[len(amount)-1]} D{d[len(d)-1]}" 
                result=f"\nRolls:{numlist}\n\n***Total {total}***"
                embed = nextcord.Embed(
                title=embedTitle,
                description=f"{result}",
 
                )
                embed_message = await interaction.response.send_message(embed=embed)
                embed_message = await embed_message.fetch()
                #await interaction.response.send_message(result)
                if reject==True:
                        await interaction.response.send_message(f"{triggernumD} is out of range. please choose a value between 2 and 100")
            
        else:
            await interaction.response.send_message(f"Not a valid entry")
            #properly fix later
            return
def setup(bot):
    bot.add_cog(dice_roller(bot))