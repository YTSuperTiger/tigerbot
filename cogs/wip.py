import discord
from discord import app_commands
from discord.ext import commands
import traceback

TEST_GUILD = discord.Object(1010532040858419231)

class Feedback(discord.ui.Modal, title='Feedback'):
  name = discord.ui.TextInput(
      label='Name',
      placeholder='Your name here...',
  )
  feedback = discord.ui.TextInput(
      label='What do you think of this new feature?',
      style=discord.TextStyle.long,
      placeholder='Type your feedback here...',
      required=False,
      max_length=300,
  )

  async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}!', ephemeral=True)

  async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        traceback.print_tb(error.__traceback__)

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        self.stop()

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Cancelling', ephemeral=True)
        self.value = False
        self.stop()
      
class wip(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  
  @app_commands.guilds(1010532040858419231)
  @app_commands.command(description="Submit feedback")
  async def feedback(self, interaction: discord.Interaction):
      await interaction.response.send_modal(Feedback())
  @commands.command()
  async def viewmodel(self, ctx):
    view = Confirm()
    await ctx.send('Do you want to continue?', view=view)
    await view.wait()

    
async def setup(bot):
  await bot.add_cog(wip(bot))