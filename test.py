import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
ver = os.getenv("Version")

class testCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(description="For Testing, [DEV ONLY]")
    async def test(self, ctx:discord.ApplicationContext):
        testEmb = discord.Embed(title="**Testing Dialog**", description="*__For Science Porposes__*", color=0x56B9CD)
        testEmb.add_field(name="**__What's Being Tested__**", value="```Doing Code in a Different Document```")
        testEmb.set_footer(text=ver)
        await ctx.respond(embed=testEmb)

def setup(bot):
    bot.add_cog(testCommand(bot))