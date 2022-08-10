import discord
from discord import option
from discord.ext import commands

import os
import json
from dotenv import load_dotenv

class kudoGive(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.devList = []
    
    @commands.slash_command(description="Give Kudos To A team Member")
    @option('member',required=True)
    async def kudos(self,ctx:discord.ApplicationContext,member:discord.Member):
        with open('profiles.json','r') as read:
            self.devList.clear()
            file = json.load(read)
            for dev in file:
                self.devList.append(dev)
            for person in self.devList:
                if member.nick == person['nick']:
                    person['kudos'] += 1
            with open('profiles.json', 'w') as outfile:
                json.dump(self.devList,outfile)
        await ctx.respond(f"{ctx.author.nick} Gave Kudos to {member.nick}",delete_after=3)

def setup(bot):
    bot.add_cog(kudoGive(bot))

