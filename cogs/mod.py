import discord
import time
from time import gmtime, strftime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class moderation1(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  def keycheck(id):
    if db["{0}.setup".format(id)] == True:
      return True
    else: 
      return False
      
  @commands.command(name="ban")
  async def ban(self, ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed=discord.Embed(title="User Banned!", description="**{0}** was banned by **{1}** for **{3}**!".format(member, ctx.message.author, reason), color=0xff00f6)
    await bot.say(embed=embed)
    
  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Insert a member to ban!!! :rolling_eyes:')
  @has_permissions(kick_members=True)
  @commands.command()
  async def mute(self, ctx, member: discord.member, *, reason=None):
    role = discord.utils.find(lambda r: r.name == 'Muted', ctx.message.guild.roles)
    await member.add_roles(role)
    embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for **{3}**!".format(member, ctx.message.author, reason), color=0xff00f6)
    await bot.say(embed=embed)
    
  @has_permissions(ban_members=True)
  @commands.command(name="lockdown")
  async def lockdown(self, ctx):
    channel = ctx.channel
    await ctx.channel.set_permissions(ctx.message.guild.default_role, send_messages=False)
    await ctx.send("Locked channel")
  @commands.command(name="unlock")
  async def unlock(self, ctx):
    if ctx.message.author.guild_permissions.administrator:
      channel = ctx.channel
      await ctx.channel.set_permissions(ctx.message.guild.default_role, send_messages=True)
      await ctx.send("Unlocked channel")
    else:
      await ctx.send("Failed to unlock channel. This could be a sign of missing permissions or a backend error")



async def setup(bot):
  await bot.add_cog(moderation1(bot))