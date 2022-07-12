
from cProfile import label
import os
from click import style
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption,Select
from matplotlib.style import context




load_dotenv()
ver = os.getenv('versionNumb')


class TestCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def test(self, ctx):
        bot = self.bot
        embed = discord.Embed(title="Test Dialog",description="For Testing Command Concepts or Command Funcitons",color=0x56B9CD)
        embed.add_field(name="__What's being Tested__", value="``Buttons``")
        embed.set_footer(text=ver)
        await ctx.send(embed=embed,components=[Button(label="TestB1", style='1',custom_id="test1")])
        await ctx.message.delete()
        
