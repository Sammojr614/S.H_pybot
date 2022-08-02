import os
import sys
import traceback
from dotenv import load_dotenv


# Discord Imports
import discord
from discord.ext import commands
import discord.ext.commands.errors
from discord.ext.commands.errors import *


# Commands
from errorNet import CommandErrorHandler
from test import testCommand
from vote import callVote
from help import helpCommand
from profile import makeProfile



# loading some stuff from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CREATOR_ID = os.getenv("CREATOR_ID ")
ver = os.getenv("versionNumb")

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="-", help_command=None,intents=intents)






@bot.event
async def on_ready():
    print(f"{bot.user.name} is Ready for commands!")
    await bot.change_presence(activity=discord.Game(name="Crusading Isles Beta"))

    bot.add_cog(CommandErrorHandler(bot))

    bot.add_cog(helpCommand(bot))

    bot.add_cog(testCommand(bot))

    bot.add_cog(callVote(bot))
    
    bot.add_cog(makeProfile(bot))

   

@bot.event
async def on_reaction_add(reaction,user):
    total_votes = 0
    thumbs_up = 0
    thumbs_down = 0
    if user == bot.user:
        return
    if reaction.emoji == "\U0001F44D":
        total_votes += 1
        thumbs_up += 1
    elif reaction.emoji == "\U0001F44E":
        total_votes += 1
        thumbs_down += 1


    
# Testing Interations 
bot.run(TOKEN)

    
   
