import discord
import time
from time import gmtime, strftime
from discord.ext import commands

bot = commands.Bot(command_prefix = '*')

class trigger(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    
  @bot.event
  async def on_message(message):
    msg_cnt = message.content.lower()
    if "thisisbotdeletetest" in msg_cnt:
        await message.delete()
      
def setup(bot):
  bot.add_cog(trigger(bot))