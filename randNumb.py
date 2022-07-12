import os
import discord
from discord.ext import commands
import random

from dotenv import load_dotenv

load_dotenv()
ver = os.getenv('versionNumb')

class randNumb(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(pass_context = True)
    async def randNumb(self,ctx, args):
        embed = discord.Embed(title="Random Number Generator", color=0x56B9CD)
        randNumbe = random.randint(0, int(args))
        embed.add_field(name="__Set Max__", value=f"``{args}``", inline=False)
        embed.add_field(name="__Generated Number__", value=f"``{randNumbe}``", inline=False)
        embed.set_footer(text=ver)
        await ctx.send(embed=embed)

