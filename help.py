import discord
from discord.ext import commands

import os
from dotenv import load_dotenv


class helpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.helpEmb = discord.Embed(title='**Soaring Hero Commads**', description="*All of the Commands for this bot*",color=0x56B9CD)

    @commands.slash_command(description="A list of all the commands for the bot")
    async def help(self,ctx:discord.ApplicationContext):
        self.helpEmb.add_field(name="1.**__Profile__**",value="``this Command Allows you to Adjust and See your profile``",inline=False)
        self.helpEmb.add_field(name="2.**__Vote__**",value="``For couting votes``",inline=False)
        await ctx.respond(embed=self.helpEmb)

def setup(bot):
    bot.add_cog(helpCommand(bot))