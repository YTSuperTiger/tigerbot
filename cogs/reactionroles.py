import discord
import time
from time import gmtime, strftime
from discord.ext import commands

class trigger(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    
      
async def setup(bot):
  await bot.add_cog(trigger(bot))