import discord
from discord.ext import commands
import json
from dotenv import load_dotenv
import os


load_dotenv()
ver = os.getenv("Version")


class Writefile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def filewrite(self, ctx, args1, *args2):
        await ctx.message.delete()
        testWrite = [{
            "name": ctx.message.author.name,
            "testValue": "{}".format(" ".join(args2))
        }]
        if args1.lower() == "write":
            for name in testWrite:
                if name['name'] != ctx.message.author.name:
                    testWrite.append({
                        "name": ctx.message.author.name,
                        "testValue": "{}".format(" ".join(args2))
                    })

            with open("test.json", "w") as outfile:
                json.dump(testWrite, outfile)
        elif args1.lower() == 'read' or args1 == None and args2 == None:
            with open('test.json', 'r') as openFile:
                json_object = json.load(openFile)
                for i in json_object:
                    if i["name"] == f"{ctx.message.author.name}":
                        jsonEmbed = discord.Embed(
                            title="What's Written", color=0x56B9CD)
                        jsonEmbed.add_field(
                            name="Whom", value="```"+i["name"] + "```")
                        jsonEmbed.add_field(
                            name="What's Written", value="```"+i["testValue"] + "```", inline=False)
                        jsonEmbed.set_footer(text=ver)
                        await ctx.send(embed=jsonEmbed)
                    else:
                        jsonEmbed = discord.Embed(
                            title="What's Written", color=0x56B9CD)
                        jsonEmbed.add_field(
                            name="Whom", value="You don't have anything")
                        jsonEmbed.set_footer(text=ver)
                        await ctx.send(embed=jsonEmbed)
