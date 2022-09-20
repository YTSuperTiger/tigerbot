import discord
import time
from discord import app_commands
from time import gmtime, strftime
from discord.ext import commands

class update(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(name="test", guild_ids=[1010532040858419231])
  async def test(ctx):
    await ctx.respond("Yay")


    




async def setup(bot):
  await bot.add_cog(update(bot))