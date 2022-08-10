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
    def __init__(self, bot):
        self.bot = bot
        self.devList = []
        self.messsage_id = 0


    #for updating Stuff
    def update(self,fromdb,ctx,toDb):
        self.devList.clear()
        with open('profiles.json', 'r') as read:
            file = json.load(read)
            for user in file:
                self.devList.append(user)
                for dev in self.devList:
                    if dev['nick'] == ctx.author.nick:
                        dev[fromdb] = toDb
                with open('profiles.json', 'w') as outfile:
                    json.dump(self.devList, outfile)

    @commands.slash_command(description="Messing with Your profile")
    @option("role", description="Your role in the company", required=False)
    @option("goal", description="Wrting your sprint goal", required=False)

    #The Actual Command 
    async def profile(self, ctx: discord.ApplicationContext, goal: str, role: str):
        self.devList.clear()
        profEmb = discord.Embed(title="**__Your Profile__**", color=0x56B9CD)
        profEmb.set_footer(text=ver)
        #if the Document is empty
        if os.stat("profiles.json")[stat.ST_SIZE] == 0:
            action = await ctx.respond("Creating profiles Please Run again to see yours", delete_after=5)
            message = await action.original_message()

            guild = self.bot.get_guild(message.author.guild.id)
            role = discord.utils.get(
                message.guild.roles, name='Soaring Heroes')

            for member in guild.members:
                if role in member.roles and not member.bot:
                    self.devList.append(
                        {'name': f"{member}", "nick": f"{member.nick}", "role": "Unassigned","kudos":0, "goal": "Nothing yet"})

            with open('profiles.json', 'w') as outfile:
                json.dump(self.devList, outfile)
                outfile.close()
        else:
            #So it Sends the Dialog when There's no Input
            if len(ctx.unselected_options) == 2:
                with open('profiles.json', 'r') as read:
                    file = json.load(read)
                    for user in file:
                        if user['nick'] == ctx.author.nick:
                            profEmb.add_field(name="__Company Role__", value=f"*{user['role']}*", inline=False)
                            profEmb.add_field(name=f"**Kudos**",value=f"``{user['kudos']}``")
                            profEmb.add_field(name=f"**__Sprint Goal__**", value=f"```{user['goal']}```",inline=False)
                            profEmb.set_author(name=user['name'], icon_url=ctx.author.avatar.url)
                            action = await ctx.respond(embed=profEmb)
                            message = await action.original_message()
                            await message.add_reaction('\U0000274C')
                            self.messsage_id = message.id
            else:
                for option in ctx.selected_options:
                    if option['name'] == 'goal':
                        self.update('goal',ctx,goal)
                        await ctx.respond("Sprint Goal Updated!",delete_after=3)
                    elif option['name'] == 'role':
                        self.update('role',ctx,role)
                        await ctx.respond("Company Role Update!",delete_after=3)

    #Reactions
    @discord.Cog.listener()
    async def on_raw_reaction_add(self,payload:discord.RawReactionActionEvent):
        #if the reaction isn't from this message, do Nothing
        if self.messsage_id != payload.message_id:
            return
        else:
            #if the Reactor isn't a bot
            if not payload.member.bot:
                guild = self.bot.get_guild(payload.guild_id)
                channel = guild.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                await message.remove_reaction('\U0000274C',payload.member)
                await message.delete()

        



def setup(bot):
    bot.add_cog(profile(bot))
