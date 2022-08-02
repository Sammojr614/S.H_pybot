import json
import discord
from discord.ext import commands

import os
import json
from dotenv import load_dotenv

load_dotenv()

class fileWrite(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def writeToFile(self,ctx,*args):
        discordEm = discord.Embed(title="Successful Write!")
        discordEm.add_field(name="The File has been Written to!")
        await ctx.message.delete()
        storage = [{'name': ctx.message.author.name,
        'value': '{}'.format(" ".join(args))}]
        with open('storage.json', 'w') as outfile:
            json.dump(storage,outfile)

        with open('storage.json','r') as readfile:
            file = json.load(readfile)
            for i in file:
                if i['name'] != ctx.message.author.name:
                    storage = [{'name':file[i]['name'],
        'value': file[i]['value']},{'name': ctx.message.author.name,
        'value': '{}'.format(" ".join(args))}]
        await ctx.send("Successfully Written!")

                

        




