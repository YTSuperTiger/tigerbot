import discord, time, asyncio, math, random, traceback, sys
from async_timeout import timeout
from time import gmtime, strftime
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import has_permissions

cog = commands.Cog()

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def sacrifice(self, ctx, member : discord.Member, owdi):
    embed=discord.Embed(color=0xff0000)                    
    embed.add_field(name="Sacrifice", value=f"{member} has been ```SACRIFICED``` to {0}".format(owdi), inline=False)
    embed.add_field(name="Respects", value="Pay your respects by sending "F" in the chat below.", inline=True)
    await ctx.send(embed=embed)


  @commands.command(name="hello", aliases=["hi"])
  async def say_hello(self, ctx):
    await ctx.send(f"{choice(('Hello', 'Hi', 'Hey', 'Hiya'))} {ctx.author.mention}!")


  @commands.command(name="echo", aliases=["say"])
  async def echo_message(self, ctx, *, message):
    await ctx.send(message)
    
  @commands.command(name="tellmeajoke")
  async def tellmeajoke(self, ctx):
      randoma = random.randint(1,3)
      if randoma == 1:
        await ctx.send("What gets wet the more it dries? A towel")
      if randoma == 2:
        await ctx.send("What has four wheels and flies? A garbage truck")
      if randoma == 3:
        await ctx.send("You are a joke for running this command 😂")

  @commands.command(name="uwu")
  async def uwu(self, ctx):
      await ctx.send("Fuck off") 
  @commands.command(name="echoembed")
  async def echoembed(self, ctx, message):
    em = discord.Embed(color=0x679f58)
    em.set_author(name="{0}".format(ctx.author), icon_url=ctx.author.avatar_url)
    em.add_field(name="Echo", value="{0}".format(message), inline=False)
    await ctx.send(embed=em)
def setup(bot):
	bot.add_cog(Fun(bot))