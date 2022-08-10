import discord
from discord.ext import commands


import os 
from dotenv import load_dotenv

load_dotenv()
ver = os.getenv("Version")

class linkCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.linkEmb = discord.Embed(title="**Important Links**",description="__Links That we Need__",color=0x56B9CD)
        self.linkEmb.set_footer(text=ver)
    
    @commands.slash_command()
    async def links(self,ctx:discord.ApplicationContext):
        self.linkEmb.add_field(name="**__Google Drive__**", value="[Click Here](https://drive.google.com/drive/folders/18jYizTmzGltxY9QW-JFLiKzMSrMwKlpj?usp=sharing)",inline=False)
        self.linkEmb.add_field(name="**__Trello Board__**",value="[Click Here](https://trello.com/b/Yh8Shm5S/crusading-isles)",inline=False)
        await ctx.respond(embed=self.linkEmb)
    

def setup(bot):
    bot.add_cog(linkCommand(bot))

