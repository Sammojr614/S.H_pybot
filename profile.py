import discord
from discord import option
from discord.ext import commands

import os
import json
import stat
from dotenv import load_dotenv

load_dotenv()
ver = os.getenv("Version")

class profile(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.devList = []

    @commands.slash_command()
    @option("write",description="Wrting your discription",required=False)
    async def profile(self,ctx:discord.ApplicationContext,write:str):
        self.devList.clear()
        profEmb = discord.Embed(title="**__Your Profile__**", description="*__Your Work Profile__*", color=0x56B9CD)
        profEmb.set_footer(text=ver)
        if os.stat("storage.json")[stat.ST_SIZE] == 0:
            action = await ctx.respond("Creating profiles Please Run again to see yours")
            message = await action.original_message()

            guild = self.bot.get_guild(message.author.guild.id)
            role = discord.utils.get(message.guild.roles,name='Soaring Heroes')

            for member in guild.members:
                if role in member.roles and not member.bot:
                    self.devList.append({'Discord Name': f"{member}", "nick": f"{member.nick}","description": "Nothing yet"})

            with open('storage.json','w') as outfile:
                    json.dump(self.devList,outfile)
                    outfile.close()
        else:
            if write is None:
                with open('storage.json','r') as read:
                    file = json.load(read)
                    for user in file:
                        if user['nick'] == ctx.author.nick:
                            profEmb.add_field(name=f"**__{user['nick']}'s Profile__**", value=f"``{user['description']}``")
                            profEmb.set_author(name=user['Discord Name'])
                            await ctx.respond(embed=profEmb)

            else:
                self.devList.clear()
                with open('storage.json','r') as read:
                    file = json.load(read)
                    self.devList.append(file)
                    print(self.devList)
                    
                            
                   
                
                            
                                






def setup(bot):
    bot.add_cog(profile(bot))
    
