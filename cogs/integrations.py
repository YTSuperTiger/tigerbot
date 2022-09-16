import discord, time
from replit import db
from time import gmtime, strftime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
# create a key with a value - db["key"] = "value"
# Get a keys value - db["key"]
# Delete a key - del db["key"]

bot = commands.Bot(command_prefix = '*')

class integration(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    
  def setup(self,bot):
    id = ctx.message.guild.id
    db["{0}.setup".format(id)] = True
    ctx.send("Welcome to the setup, please start by setting a audit log channel.")
    #read response from user
    db["{0}.auditlog".format(id)] = #insert audit log channel id
    ctx.send("Please set moderator roles for the sever")
    #read response from user
    db["{0}.mod".format(id)] = #insert moderator roles
    #insert other defined guild oriented information for key storage
    ctx.send("Would you like to make the reasons for warns and bans optional?")
    db["{0}.optional".format(id)] = #insert bool


def setup(bot):
  bot.add_cog(integration(bot))