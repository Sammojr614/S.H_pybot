import os
from click import pass_context
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
ver = os.getenv("versionNumb")
class commandHelp(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def help(self,ctx):
        bot = self.bot
        embed = discord.Embed(title="Help Menu",describe="``The Help list for all of my Commands``",color=0x56B9CD)
        embed.add_field(name="test", value="Use this command to test things", inline=False)
        embed.add_field(name="randNumb [value]", value="``Random Number Generator with [value] being the max``", inline=False)
        embed.set_footer(text=f"Ver {ver}")
        await ctx.send(embed=embed)
