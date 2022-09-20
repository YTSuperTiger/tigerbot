import discord
import time
from time import gmtime, strftime
from discord.ext import commands
from discord import ui

class modal(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  class Questionnaire(ui.Modal, title='Questionnaire Response'):
      name = ui.TextInput(label='Name')
      answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)
  
      async def on_submit(self, interaction: discord.Interaction):
          await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)
  
      
async def setup(bot):
  await bot.add_cog(modal(bot))