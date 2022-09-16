from discord import Webhook, RequestsWebhookAdapter 
import discord
import time
from time import gmtime, strftime
from discord.ext import commands

bot = commands.Bot(command_prefix = '*')

class webhook(commands.Cog):

  def __init__(self, bot):
    intents = discord.Intents(messages=True, guilds=True)
    self.bot = bot(intents=intents)
    
  @bot.command
  async def webhook(self, ctx, info):
    webhook = Webhook.from_url('webhook-url-here', adapter=RequestsWebhookAdapter())
    
    webhook.send(content="Hello World") 
def setup(bot):
  bot.add_cog(webhook(bot))