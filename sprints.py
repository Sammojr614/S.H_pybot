
import discord
from discord.ext import commands
import os


from dotenv import load_dotenv

load_dotenv()

ver = os.getenv("versionNumb")

class saveSprint(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def sprint(self,ctx):
        file = open("sprints.txt")
        await ctx.message.delete()
        sprintEmbed = discord.Embed(title="__Sprint Schedule__",discription="A Reminder of Our Sprint Schedule", color=0x56B9CD)
        sprintEmbed.add_field(name="Sprint",value="```" + file.read() +"```")
        sprintEmbed.set_footer(ver)
        await ctx.send(embed=sprintEmbed)
            
            

