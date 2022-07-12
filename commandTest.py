
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
ver = os.getenv('versionNumb')

class TestCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def test(self, ctx):
        embed = discord.Embed(title="Test Dialog",color=0x56B9CD)
        embed.set_footer(text=ver)
        await ctx.send(embed=embed)

