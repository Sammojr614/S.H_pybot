
import discord
from discord import option
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
ver = os.getenv('Version')

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents,command_prefix="-")



#When the Bot Starts
@bot.event
async def on_ready():
    print(f"Bot is up")
    await bot.change_presence(activity=discord.Game(name="Crusading isles Beta"))

#Test Command
bot.load_extension('test', store=False)

#The Vote Command
bot.load_extension('vote',store=False)

#The Profile Command
bot.load_extension('profile', store=False)
  
#A Meeting Reminder
bot.load_extension('remind',store=False)

bot.run(token)