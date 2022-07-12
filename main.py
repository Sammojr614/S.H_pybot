import os
from pydoc import describe
from turtle import color, title
from unicodedata import name


import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord.ext.commands.errors
from discord.ext.commands.errors import *


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
try:

    # Testing Command
    @bot.command(name='test', help="a Command to Test Stuff")
    async def test(ctx):
        response = "This Works!"
        await ctx.send(response)

    #Rng
    @bot.command(name='randNumb', help="Returns a Random Number")
    async def randNumb(ctx, args):
        randNumbe = random.randint(0, int(args))
        response = randNumbe
        await ctx.send(response)
    #Dm Command
    @bot.command(pass_context=True)
    async def dm(ctx,user: discord.User,*,message=None):
        message = message or "This message was Sent Via DM "
        await user.send(message)

    @bot.command(name = 'help')
    async def help(ctx):
        embed = discord.Embed(title="Help Menu",describe="The Help list for all of my Commands",color=0x56B9CD)
        embed.add_field(name="test", value="Use this command to test things", inline=False)
        embed.add_field(name="randNumb [value]", value="Random Number Generator with [value] being the max", inline=False)
        embed.set_footer(text=f"Ver {ver}")
        await ctx.send(embed=embed)
    bot.run(TOKEN)
except MissingRequiredArgument :
    user = bot.fetch_user(CREATOR_ID)
    user.send("``[ERROR!]``` \n __Type:__ **MissngRequiredArgument** ")
    bot.run(TOKEN)

