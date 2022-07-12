
import os
import discord
from discord.ext import commands



class TestCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def test(self, ctx):
        embed = discord.Embed(title="Test Dialog",color=0x56B9CD)
        await ctx.send(embed=embed)

