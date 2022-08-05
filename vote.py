import discord
from discord.ext import commands
from discord import option

import os
from dotenv import load_dotenv

load_dotenv()
ver = os.getenv("Version")

class voteCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(description="For Doing Votes on Things")
    @option('vote', require=True)
    async def callvote(self,ctx:discord.ApplicationContext,call:str):
        voteEmb = discord.Embed(title="**__Vote!__**",description="*__Vote On This__*",color=0x56B9CD)
        voteEmb.add_field(name="__What's Being Voted on__", value=f"```{call}```")
        voteEmb.set_footer(text=ver)
        action = await ctx.respond(embed=voteEmb)
        message = await action.original_message()
        await message.add_reaction('\U0001F44D')
        await message.add_reaction('\U0001F937')
        await message.add_reaction('\U0001F44E')

def setup(bot):
    bot.add_cog(voteCommand(bot))