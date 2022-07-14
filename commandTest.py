
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import discord.ext.commands.errors
from discord.ext.commands.errors import *


load_dotenv()
ver = os.getenv('versionNumb')


class TestCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def test(self,ctx,args):
        embed = discord.Embed(title="Test Dialog", description="For Testing Command Concepts or Command Funcitons", color=0x56B9CD)
        embed.add_field(name="__What's being Tested__",value="``Error handling, and Debugging Stuff``", inline=False)
        embed.add_field(name="__Debug Log__",value=f"Args: {args}", inline=False)
        embed.set_footer(text=f"{ver}")
        await ctx.send(embed=embed)
        await ctx.message.delete()