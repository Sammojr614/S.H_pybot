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
from filewrite import Writefile

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

    bot.add_cog(CommandErrorHandler(bot))

    bot.add_cog(testCommand(bot))

    bot.add_cog(Writefile(bot))

    
# Testing Interations 
bot.run(TOKEN)

    
   
