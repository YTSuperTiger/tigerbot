import discord
import time
from time import gmtime, strftime
from discord.ext import commands

class trigger(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    
  @commands.event
  async def on_message(message):
    msg_cnt = message.content.lower()
    if "thisisbotdeletetest" in msg_cnt:
        await message.delete()
      
async def setup(bot):
  await bot.add_cog(trigger(bot))