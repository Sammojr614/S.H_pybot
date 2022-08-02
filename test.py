import discord 
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
ver = os.getenv("Version")

class testCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def test(self,ctx):
        await ctx.message.delete()
        testEmbed = discord.Embed(title="Test Dialog", discription="For testing Stuff",color=0x56B9CD)
        testEmbed.add_field(name="__What's Being Tested__", value="```Finding the Amount of Members```",inline=False )
        testEmbed.add_field(name="*__Debug Log__*",value=f"```The List Was Printed in the Terminal```",inline=False)
        guild = self.bot.get_guild(ctx.author.guild.id)
        for members in guild.members:
            print(members)
        
        
        
        
        testEmbed.set_footer(text=ver)
        await ctx.send(embed=testEmbed) 