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
        testEmbed.add_field(name="*__Debug Log__*",value=f"```The Member list is below```",inline=False)
        guild = self.bot.get_guild(ctx.author.guild.id)
        role = discord.utils.find(lambda r: r.id == '955310316001046588',ctx.guild.roles)
        for member in guild.members:
            if role in member.roles:
                testEmbed.add_field(name="Soaring Hero Devs", value=member)

            
        testEmbed.set_footer(text=ver)
        await ctx.send(embed=testEmbed) 