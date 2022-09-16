@client.command()
async def clear(ctx, amount=1):
    member = ctx.message.author
    aamount = amount + 1
    await ctx.channel.purge(limit=aamount)
    msg = await ctx.send('Cleared ' + str(amount) + ' messages')
    cchannel = ctx.channel
    channel = client.get_channel(781220833477132288)
    embed=discord.Embed(title="Audit Log", description="Command Detection", color=0xff8040)
    embed.add_field(name=f"{member} has cleared {amount} messages in #" + str(cchannel) + 'at' + strftime("%a, %d %b %Y %I:%M:%S %p", gmtime()), value="Action", inline=False)
    embed.set_footer(text="{}".format(ctx.message.author))
    await channel.send(embed=embed)
    time.sleep(3)
    await msg.delete()
  