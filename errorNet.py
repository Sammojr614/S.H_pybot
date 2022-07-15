import discord
import traceback
import sys
from discord.ext import commands
import os
from dotenv import load_dotenv



load_dotenv()
ver = os.getenv('Version')


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
       
      
    @commands.Cog.listener()
    
    async def on_command_error(self,ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return
        #if the command is disabled
        if isinstance(error, commands.DisabledCommand):
            await ctx.message.delete()
            embed = discord.Embed(title="[ ERROR! ]",description="*There was an error*", color=0xFF3333)
            embed.add_field(name="__Error Discription__", value="This Command is Disabled")
            embed.set_footer(text=f"{ver}")
            await ctx.send(embed=embed)

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                await ctx.send('I could not find that member. Please try again.')

        #Missing an Argument
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            embed = discord.Embed(title="[ ERROR! ]",description="*There was an error*", color=0xFF3333)
            embed.add_field(name="__Error Discription__", value="``You forgot to Give a Letter or Number for Input``")
            embed.set_footer(text=f"{ver}")
            await ctx.send(embed=embed)

        else:
            print('Ignoring exception in command {}:'.format(
                ctx.command), file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)
