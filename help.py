import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()
ver = os.getenv('Version')

class helpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self,ctx):
        await ctx.message.delete()
        helpEmbed = discord.Embed(title="**__Help Menu__**",description="__A list of the Commands__",color=0x56B9CD)
        helpEmbed.add_field(name="__test__",value="```A dialog that's for testing things```",inline=False)
        helpEmbed.add_field(name="__vote__", value="```To do votes, how to use: vote [string]```", inline=False)
        helpEmbed.add_field(name="__filewrite__",value="```writing to a file, Mainily for testing file writing, to use: filewrite [write] [string] or filewrite[read] [string]```")
        helpEmbed.set_footer(text=ver)
        await ctx.send(embed=helpEmbed)
