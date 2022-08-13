from cgi import test
from tkinter import Button
import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
ver = os.getenv("Version")

class testButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Press Me",
            style=discord.ButtonStyle.primary,
            custom_id="testBtn",
        )
    
    async def callback(self, interaction: discord.Interaction):
        testEmb = discord.Embed(title="Test Dialog",description="*__For Science__*",color=0x56B9CD)
        testEmb.add_field(name="**__What's Being Tested__**", value="```Button Pressed```")
        await interaction.message.edit(embed=testEmb)
        
        
class deleteButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="\U0000274C",
            style=discord.ButtonStyle.danger,
            custom_id="testBtn2"
        )
    async def callback(self,interaction: discord.Interaction):
        await interaction.message.delete()

class testCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.message_id = 0

    @commands.slash_command(description="For Testing, [DEV ONLY]")
    async def test(self, ctx:discord.ApplicationContext):
        vi = discord.ui.View()
        vi.add_item(testButton())
        vi.add_item(deleteButton())
        testEmb = discord.Embed(title="Test Dialog",description="*__For Science__*")
        testEmb.add_field(name="**__What's Being Tested__**", value="```Using Buttons```")
        action = await ctx.respond(embed=testEmb, view=vi)
        message = await action.original_message()


def setup(bot):
    bot.add_cog(testCommand(bot))