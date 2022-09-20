import discord, sys
import time
from discord import app_commands
from time import gmtime, strftime
from discord.ext import commands

class slash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="echo", description="Echo a user input")
  async def echo(interaction: discord.Interaction, message):
    await interaction.response.send_message("{0}".format(message))

async def setup(bot):
  await bot.add_cog(slash(bot))