import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
ver = os.getenv("Version")

class removeBtn(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="\U0000274C",
            style=discord.ButtonStyle.danger,
        )

    async def callback(self,interaction:discord.Interaction):
        await interaction.message.delete()


class helpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.helpEmb = discord.Embed(title='**Soaring Hero Commads**', description="*All of the Commands for this bot*",color=0x56B9CD)

    @commands.slash_command(description="A list of all the commands for the bot")
    async def help(self,ctx:discord.ApplicationContext):
        vi = discord.ui.View()
        vi.add_item(removeBtn())
        self.helpEmb.add_field(name="1.**__Profile__**",value="``this Command Allows you to Adjust and See your profile``",inline=False)
        self.helpEmb.add_field(name="2.**__Vote__**",value="``For couting votes``",inline=False)
        self.helpEmb.add_field(name="3.**__test__**", value="``For Testing things``",inline=False)
        self.helpEmb.add_field(name="4.**__kudos__**",value="``For Rewarding teammates``",inline=False)
        self.helpEmb.set_footer(text=ver)
        await ctx.respond(embed=self.helpEmb,view=vi)

def setup(bot):
    bot.add_cog(helpCommand(bot))