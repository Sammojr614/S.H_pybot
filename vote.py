import discord
from discord.ext import commands



class callVote(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(pas_context=True)
    async def vote(self,ctx,*args):
        await ctx.message.delete()
        voteEmbed = discord.Embed(title="Vote", color=0x56B9CD)
        voteEmbed.add_field(name="What's being Voted on", value="```" + " ".join(args) + "```")
        message = await ctx.send(embed=voteEmbed)
        await message.add_reaction("\U0001F44D")
        await message.add_reaction("\U0001F44E")

