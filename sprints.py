from click import pass_context
import discord
from discord.ext import commands
import io
import sys

class saveSprint(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context = True)
    async def sprint(self,ctx, args):
        if args.lower() == "current":
            file = open("sprints.txt")
            await ctx.message.delete()
            await ctx.send(file.read())
            

