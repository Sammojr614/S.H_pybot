import discord 
from discord import option
from discord.ext import commands

import os
from dotenv import load_dotenv

class remindcommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command()
    @option("day",required=False)
    async def remind(self,ctx:discord.ApplicationContext,day:int):
        await ctx.respond("This command is still in the works", delete_after=5)
        
        

def setup(bot):
    bot.add_cog(remindcommand(bot))
