import os


import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord.ext.commands.errors
from discord.ext.commands.errors import *


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix="-")
# Starting the Bot
@client.event
async def on_ready():
    user = await client.fetch_user(530609301794848781)
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
    bot.run(TOKEN)
except MissingRequiredArgument :
    user = bot.fetch_user(530609301794848781)
    user.send("``[ERROR!]``` \n __Type:__ **MissngRequiredArgument** ")
    bot.run(TOKEN)

