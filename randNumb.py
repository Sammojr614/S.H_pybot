from turtle import title
from click import pass_context
import discord
from discord.ext import commands
import random

class randNumb(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(pass_context = True)
    async def randNumb(self,ctx, args):
        embed = discord.Embed(title="Random Number Generator", color=0x56B9CD)
        randNumbe = random.randint(0, int(args))
        embed.add_field(name="__Set Max__", value=f"``{args}``", inline=False)
        embed.add_field(name="__Generated Number__", value=f"``{randNumbe}``", inline=False)
        await ctx.send(embed=embed)

