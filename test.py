import discord 
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
ver = os.getenv("Version")

class testCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def test(self,ctx):
        await ctx.message.delete()
        testEmbed = discord.Embed(title="Test Dialog", discription="For testing Stuff",color=0x56B9CD)
        testEmbed.add_field(name="__What's Being Tested__", value="```Looking at the ctx.author.name```", )
        testEmbed.add_field(name="*__Debug Log__*",value=f"```{ctx.message.author.name}```",inline=False)
        testEmbed.set_footer(text=ver)
        await ctx.send(embed=testEmbed) 