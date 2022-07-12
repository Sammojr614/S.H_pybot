
import os
from dotenv import load_dotenv


#Discord Imports
import discord
from discord.ext import commands
import discord.ext.commands.errors
from discord.ext.commands.errors import *

#Commands 
from commandTest import TestCommand
from randNumb import randNumb
from helpCommand import commandHelp

#loading some stuff from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CREATOR_ID = os.getenv("CREATOR_ID ")
ver = os.getenv("versionNumb")

client = discord.Client()
bot = commands.Bot(command_prefix="-",help_command=None)
# Starting the Bot
@client.event
async def on_ready():
    user = await client.fetch_user(CREATOR_ID)
    await user.send("PyBot is Up and Running!")


@bot.event
async def on_ready():
    print(f"{bot.user} Has Connected to Discord!")
    await bot.change_presence(activity=discord.Game(name="Crusading Isles Beta"))
try:

    # Testing Command
    bot.add_cog(TestCommand(bot))

    #Rng
    bot.add_cog(randNumb(bot))

    #Our Help Command, Needs Updating every time we create a new command
    bot.add_cog(commandHelp(bot))
        
    bot.run(TOKEN)
except MissingRequiredArgument :
    user = bot.fetch_user(CREATOR_ID)
    user.send("``[ERROR!]``` \n __Type:__ **MissngRequiredArgument** ")
    bot.run(TOKEN)

