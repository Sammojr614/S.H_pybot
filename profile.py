import discord
from discord.ext import commands
from discord import Embed

from dotenv import load_dotenv
import os
import json

load_dotenv()


ver = os.getenv("Version")

class makeProfile(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def profile(self,ctx,*args):
        profileEmbed = Embed(title="Profile",discription="Your Work Profile",color=0x56B9CD)
        profileEmbed.set_footer(text=ver)
        await ctx.message.delete()
        fullArgs = " ".join(args)
        if fullArgs == '':
            with open('storage.json','r') as readfile:
                indexFile = json.load(readfile)
                for index in indexFile:
                    if index['nick'] == ctx.message.author.name:
                        if index['value'] == "":
                            profileEmbed.add_field(name=f"__{index['nick']}'s Profile__",value="``**It's Empty**``")
                        else:
                            profileEmbed.add_field(name=f"__{index['nick']}'s Profile__",value=f"``{index['value']}``")
                            
                        await ctx.send(embed=profileEmbed)
        else:
            with open('storage.json','r') as readfile:
                indexFile = json.load(readfile)
                for index in indexFile:
                    if index['nick'] == ctx.message.author.name:
                        storeThis = [{"nick": ctx.message.author.name, "value": "{}".format(" ".join(args))}]
                        with open('storage.json','w') as outfile:
                            json.dump(storeThis, outfile)
                    else:
                        storeThis.append(storeThis)
                        with open('storage.json','w') as outfile:
                            json.dump(storeThis, outfile)
                        

