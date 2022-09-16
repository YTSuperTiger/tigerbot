import discord
import time
from time import gmtime, strftime
from discord.ext import commands

bot = commands.Bot(command_prefix = '*')

class help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="help")
  async def help(self, ctx):
    embed=discord.Embed(title="Drewitt Bot")
    embed.set_thumbnail(url='')
    embed.add_field(name="Ping", value="Sends ping", inline=True)
    embed.add_field(name="Test", value="Test", inline=False)
    embed.add_field(name="Test", value="Test", inline=False)
    embed.add_field(name="Test", value="Test", inline=True)
    embed.add_field(name="Test", value="Test", inline=False)
    embed.add_field(name="Test", value="Test", inline=True)
    await ctx.send(embed=embed)


    




def setup(bot):
    bot.add_cog(help(bot))