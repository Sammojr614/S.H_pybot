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
from commandTest import TestCommand
from randNumb import randNumb
from helpCommand import commandHelp
from errorNet import CommandErrorHandler
from sprints import saveSprint

# loading some stuff from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CREATOR_ID = os.getenv("CREATOR_ID ")
ver = os.getenv("versionNumb")

client = discord.Client()
bot = commands.Bot(command_prefix="-", help_command=None)






@bot.event
async def on_ready():
    print(f"{bot.user.name} is Ready for commands!")
    await bot.change_presence(activity=discord.Game(name="Crusading Isles Beta"))

    #Error handler
    bot.add_cog(CommandErrorHandler(bot))

    # Testing Command
    bot.add_cog(TestCommand(bot))

    # Rng
    bot.add_cog(randNumb(bot))

    # Our Help Command, Needs Updating every time we create a new command
    bot.add_cog(commandHelp(bot))

    #Sprint stuff
    bot.add_cog(saveSprint(bot))
    
# Testing Interations 
bot.run(TOKEN)

    
   
