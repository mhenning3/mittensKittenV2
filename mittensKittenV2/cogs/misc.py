import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Embed

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="bubble_wrap",description="creates bubble wrap")
    async def bubble (self,interaction: nextcord.Interaction):
        sizex=20
        sizey=7
        bubb=""
        for y in range(sizey):
            bubb=bubb+"\n"
            for x in range(sizex):
                bubb=bubb+"||o||"    
        await interaction.send_message(f"{bubb}")

def setup(bot):
    bot.add_cog(misc(bot))




