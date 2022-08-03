import discord
from discord.ext import commands
from discord import Embed

from dotenv import load_dotenv
import os
import json
import stat



load_dotenv()


ver = os.getenv("Version")

class makeProfile(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.devList = []
    @commands.command(pass_context=True)
    async def profile(self,ctx,*args):
        await ctx.message.delete()
        #Title of the Embed
        profileEmbed = Embed(title="Profile",discription="Your Work Profile",color=0x56B9CD)
        #just Making sure it can see all the Arguments
        all_args = " ".join(args)
        #if there is nothing in the args
        if all_args == "":
            #Checking the File Size
            if os.stat("storage.json")[stat.ST_SIZE] == 0:
                await ctx.send("This is The first time this command has been Run, Please run again to see profile!")
                #Getting the Server and the Roles
                guild = self.bot.get_guild(ctx.author.guild.id)
                role = discord.utils.get(ctx.message.guild.roles, name='Soaring Heroes')
                #Looking at all of the memebers
                for member in guild.members:
                    if role in member.roles and not member.bot:
                        self.devList.append({'Discord Name': f"{member}", "nick": f"{member.nick}","description": "Nothing yet"})
                #Puttting everything into a file
                with open('storage.json','w') as outfile:
                    json.dump(self.devList,outfile)
                    outfile.close()
            else:
                #Finally displaying it all
                with open('storage.json','r') as read:
                    file = json.load(read)
                    for user in file:
                        if user['nick'] == ctx.message.author.nick:
                            profileEmbed.add_field(name=f"**__{user['nick']}'s Profile__**", value=f"``{user['description']}``")
                            profileEmbed.set_author(name=user['Discord Name'])
                            await ctx.send(embed=profileEmbed)
    
                        

                        
                

            
                        

       

