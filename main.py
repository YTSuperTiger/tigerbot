import discord, time, asyncio, math, random, traceback, os, youtube_dl, traceback
from async_timeout import timeout
from time import gmtime, strftime
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import has_permissions
from keep_alive import keep_alive
token = os.environ['discord_token']
keep_alive()
bot = commands.Bot(command_prefix = '^', intents=discord.Intents.all())
bot.remove_command("help")

@app_commands.guilds(1010532040858419231)
@app_commands.context_menu(name='Report to Moderators')
async def report_message(interaction: discord.Interaction, message: discord.Message):
  # We're sending this response message with ephemeral=True, so only the command executor can see it
  await interaction.response.send_message(
      f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
  )

  # Handle report by sending it into a log channel
  log_channel = interaction.guild.get_channel(0)  # replace with your channel id

  embed = discord.Embed(title='Reported Message')
  if message.content:
      embed.description = message.content

  embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
  embed.timestamp = message.created_at

  url_view = discord.ui.View()
  url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

  await log_channel.send(embed=embed, view=url_view)
@bot.command()
async def gsync(ctx):
  await bot.tree.sync()
  await ctx.send("Command Tree Synced Successfully")
@bot.command()
async def tsync(ctx):
  await bot.tree.sync(guild=discord.Object(1010532040858419231))
  await ctx.send("Command Tree Synced Successfully for guild")
  
@bot.command()
async def ping(ctx):
  await ctx.send("Pong")


@bot.event
async def on_ready():
    print("======[ BOT ONLINE! ]======")
    print ("Logged in as " + bot.user.name)
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Asher is a dissapointment.'))

@bot.command()
@commands.guild_only()
async def load(ctx, extension):
    if ctx.message.author.id == 363865768305098763:
        try:
            await bot.load_extension("cogs.{}".format(extension))
            await ctx.message.add_reaction("???")
        except discord.ext.commands.ExtensionAlreadyLoaded:
            await ctx.reply("Cog already loaded!")
        except discord.ext.commands.ExtensionNotFound:
            await ctx.message.add_reaction("???")
        except discord.ext.commands.NoEntryPointError:
            await ctx.reply("Cog doesn't have a setup function!")
        except Exception as e:
            await ctx.reply(e)

    else:
        await ctx.message.add_reaction('????')
        await asyncio.sleep(3)
        return

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("???")
        await asyncio.sleep(3)
        return

@bot.command()
@commands.guild_only()
async def unload(ctx, extension):
    if ctx.message.author.id == 363865768305098763:
        try:
            bot.unload_extension("cogs.{}".format(extension))
            await ctx.message.add_reaction("???")
        except discord.ext.commands.ExtensionNotLoaded:
            await ctx.reply("Cog wasn't loaded!")
            ctx.message.add_reaction('????')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("???")
        await ctx.reply(f"""```??? {error} ```""")

@bot.command()
@commands.guild_only()
async def reload(ctx, extension):
    if ctx.message.author.id == 363865768305098763:
        try:
            await bot.reload_extension("cogs.{}".format(extension))
        except discord.ext.commands.ExtensionNotLoaded:
            await ctx.reply("Cog wasn't loaded, attempting to load", delete_after=5)
        try:
            await bot.reload_extension("cogs.{}".format(extension))
            await ctx.message.add_reaction("???")
        except discord.ext.commands.ExtensionNotFound:
            await ctx.message.add_reaction("???")
        except discord.ext.commands.NoEntryPointError:
            await ctx.send("Cog doesn't have a setup function!", delete_after=5)
        await asyncio.sleep(5)
    else:
        await ctx.message.add_reaction('????')


@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("???")
        await ctx.reply(f"""```??? {error} ```""")
path = "./cogs"

dir_list = os.listdir(path) 
print(dir_list)
#async def load_cogs():
# for filename in os.listdir("./cogs"):
#      if filename.endswith(".py"):
#          try:
#              await bot.load_extension("cogs.{}".format(filename[:-3]))
#          except Exception as e:
#              print("========[ WARNING ]========")
#              print(f"An error occurred while loading '{filename}'""")

async def load_cogs() -> None:
    for file in os.listdir(f"./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")
                traceback.print_exc()
              
asyncio.run(load_cogs())
bot.run(token, reconnect=True)