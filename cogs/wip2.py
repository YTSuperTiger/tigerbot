import discord, time, math, random
from time import gmtime, strftime
from discord.ext import commands
from discord import app_commands
from discord.app_commands import AppCommandError

class wip2(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  @app_commands.guilds(1010532040858419231)
  @app_commands.checks.has_permissions(ban_members=True)
  @app_commands.command(name= "ban", description="Ban a user from the server, permanent. (Use command tempban for temporary bans).")
  async def ban(self, interaction: discord.Interaction, member : discord.Member, *, reason:str="No reason specified"):
    if not member or member == interaction.user:
      embed = discord.Embed(color = discord.Color.red(), title="The mentioned user cannot be banned!", description = f"It's mostly because:\n (a) The bot doesn't have permission to ban the mentioned user\n (b) You don't have the 'ban_members' permission\n (c) The bot's highest role isn't higher than {member}'s highest role\n (d) You mentioned youeself...\n (e) Backend error")
      embed.set_thumbnail(url="https://media.tenor.com/WU_r--BFSWUAAAAM/404-404error.gif")
      embed.set_author(name="{0}".format(interaction.user),icon_url=interaction.user.display_avatar)
      await interaction.response.send_message(embed=embed)
    try:
      await member.ban(reason = f"Action requested by {interaction.user}.\nReason: {reason}")
      embed=discord.Embed(title="  ~ BAN ~  ", description="User has been banned")
      embed.add_field(name="Banned User:", value="{0}".format(member), inline=False)
      embed.add_field(name="Banned by:", value="{0}".format(interaction.user), inline=False)
      embed.add_field(name="Reason:", value="{0}".format(reason), inline=False)
      embed.add_field(name="Timestamp:", value="<t:{0}:F>".format(math.ceil(time.time())), inline=False)
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/997599271291473980/1026619577779630100/IMG_1433-removebg-preview.png")
      x = random.randint(0,4)
      choice ={0:"https://media.tenor.com/9zCgefg___cAAAAC/bane-no.gif",1:"https://media.tenor.com/477PvQeAC1YAAAAC/banned.gif",2:"https://media.tenor.com/0On0_pw3TkQAAAAC/banned-thor.gif",3:"https://media.tenor.com/L-KHRnaZrqsAAAAd/nmplol-emiru.gif" ,4:"https://media.tenor.com/gqnW_Zxh2mkAAAAd/ban-banned.gif"}
      embed.set_image(url=choice[x])
      embed.color = 0xff0000
      embed.set_author(name="{0}".format(interaction.user),icon_url=interaction.user.display_avatar)
      channel = self.bot.get_channel(1013234530548723753)
      await channel.send(embed=embed)
      await interaction.response.send_message(embed=embed)
    except:
      embed = discord.Embed(color = discord.Color.red(), description = f"The mentioned user cannot be banned!\nIt's mostly because:\n (a) The bot doesn't have permission to ban the mentioned user\n (b) You don't have the 'ban_members' permission\n (c) The bot's highest role isn't higher than {member}'s highest role\n (d) You mentioned youeself...")
      await interaction.response.send_message(embed=embed)


  @app_commands.guilds(1010532040858419231)
  @app_commands.checks.has_permissions(ban_members=True)
  @app_commands.command(name= "unban", description="Unban a specified user.")
  async def unban(self, interaction: discord.Interaction, member : str, *, reason:str="No reason specified"):
    if member == interaction.user:
      embed = discord.Embed(color = discord.Color.red(), title="The mentioned user cannot be unbanned!", description = f"It's mostly because:\n (a) The bot doesn't have permission to unban the mentioned user\n (b) You don't have the 'ban_members' permission\n (c) The bot's highest role isn't higher than {member}'s highest role\n (d) You mentioned youeself...\n (e) The user is not banned\n(f) Backend error")
      embed.set_thumbnail(url="https://media.tenor.com/WU_r--BFSWUAAAAM/404-404error.gif")
      embed.set_author(name="{0}".format(interaction.user),icon_url=interaction.user.display_avatar)
      await interaction.response.send_message(embed=embed)
    try:
      await interaction.guild.unban(user=member ,reason = f"Action requested by {interaction.user}.\nReason: {reason}")
      embed=discord.Embed(title="  ~ UNBAN ~  ", description="User has been unbanned")
      embed.add_field(name="Unbanned User:", value="{0}".format(member), inline=False)
      embed.add_field(name="Unbanned by:", value="{0}".format(interaction.user), inline=False)
      embed.add_field(name="Reason:", value="{0}".format(reason), inline=False)
      embed.add_field(name="Timestamp:", value="<t:{0}:F>".format(math.ceil(time.time())), inline=False)
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/997599271291473980/1026619577779630100/IMG_1433-removebg-preview.png")
      x = random.randint(0,4)
      choice ={0:"https://media.tenor.com/aqZqWt6SMUwAAAAM/chris-chris-pill.gif",1:"https://media.tenor.com/m5fTsOZHDKgAAAAM/mineberry-read.gif",2:"https://media.tenor.com/eDiNQhC3aZcAAAAM/yea-aight-meme.gif",3:"https://media.tenor.com/ETRd-CLfGmQAAAAM/pottugets-pottu.gif" ,4:"https://media.tenor.com/h34KsaiJYSkAAAAM/saul-goodman-unbanned.gif"}
      embed.set_image(url=choice[x])
      embed.color = 0xff0000
      embed.set_author(name="{0}".format(interaction.user),icon_url=interaction.user.display_avatar)
      channel = self.bot.get_channel(1013234530548723753)
      await channel.send(embed=embed)
      await interaction.response.send_message(embed=embed)
    except:
      embed = discord.Embed(color = discord.Color.red(), title="The mentioned user cannot be unbanned!", description = f"It's mostly because:\n (a) The bot doesn't have permission to unban the mentioned user\n (b) You don't have the 'ban_members' permission\n (c) The bot's highest role isn't higher than {member}'s highest role\n (d) You mentioned youeself...\n (e) The user is not banned\n(f) Backend error")
      embed.set_thumbnail(url="https://media.tenor.com/WU_r--BFSWUAAAAM/404-404error.gif")
      embed.set_author(name="{0}".format(interaction.user),icon_url=interaction.user.display_avatar)
      await interaction.response.send_message(embed=embed)







  #@ban.autocomplete('reason')
  #async def autocomplete(interaction: discord.Interaction, current: str):
  #  reasons = ['Racism/Homophobia', 'Ban Evasion', 'Chat Spam', 'Raiding']
  #  return [app_commands.Choice(name=reason, value=reason) for reason in reasons if current.lower() in reason.lower()]
  
  @app_commands.guilds(1010532040858419231)
  @app_commands.command(name= "watermelon", description="Watermelon")
  async def watermelon(self, interaction: discord.Interaction):
    await interaction.response.send_message('{0} Watermelon 🍉'.format(interaction.user.mention)) 
  @commands.command()
  async def purgeroles(self, ctx, member: discord.Member):
    await ctx.send("Purged roles for {0}".format())




async def setup(bot):
  await bot.add_cog(wip2(bot))
  