import discord 
from discord import option
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
ver = os.getenv("Version")

class remindcommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.meetings = []
        self.remindEmb = discord.Embed(title="**Scheduled Meetings**",description="*__Upcoming Meetings__*",color=0x56B9CD)
        self.remindEmb.set_footer(text=ver)

    @commands.slash_command()
    @option("day",required=False)
    async def remind(self,ctx:discord.ApplicationContext,day:int):
        self.remindEmb.add_field(name="All Meetings", value="```Whoops This Command isn't done```")
        await ctx.respond(embed=self.remindEmb,delete_after=4)

        
        

def setup(bot):
    bot.add_cog(remindcommand(bot))
