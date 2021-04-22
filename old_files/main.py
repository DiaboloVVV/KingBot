import discord
import datetime
from dateutil import tz
import asyncio
import random
from discord.ext import commands
from dotenv import load_dotenv
from normalFunctions import *
import os
load_dotenv()

prefix = '$'
client = commands.Bot(command_prefix=prefix)

    # YOU CAN TEST IF IT WORKS
@client.command()
async def ping(message):
    await message.send(f'Pong! {round(client.latency * 1000)}ms')
    # await asyncio.sleep(0.5)
    # await mess.edit(content='Emm- hello!')


    # GETTING MENTIONED USER AVATAR
@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)



    # DISPLAYING WHEN BOT IS READY TO GO
@client.event
async def on_ready():
    print('Has been logged in as {0.user}'.format(client))



@client.command()
@commands.has_permissions(administrator=True)
async def gstart(ctx):
    await ctx.send("Answer within 15seconds.\n")
    q = ["Where do you want to host giveway? (ping the channel)",
         "How long does the giveaway should last?",
         "What is the prize?"]

    ans = []


    def validation(currentMessage):
        return currentMessage.author == ctx.author and currentMessage.channel == ctx.channel

    for i in q:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=validation)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t enter message in time')
            return
        else:
            ans.append(msg.content)
    try:
        channel_id = int(ans[0][2:-1])
    except:
        await ctx.send("You didn't ping channel properly.")
        return

    channel = client.get_channel(channel_id)

    time = convert(ans[1])
    if time == -1:
        await ctx.send("You didn't answer the time correctly. Use s|m|h|d")
        return
    elif time == -2:
        await ctx.send("Time must be an integer.")
        return
    global prize
    prize = ans[2]
    await ctx.send(f"The giveaway will be in {channel.mention} and will last {ans[1]}")

    # embed = discord.Embed(
    #     title="Giveaway!",
    #     description=f"{prize}",
    #     color= 0x006400
    # )
    # embed.add_field(
    #     name="Hosted by:",
    #     value=ctx.author.mention
    # )
    # embed.set_footer(
    #     text=f"Ends {ans[1]} from now!"
    # )
    end = datetime.datetime.utcnow() - datetime.timedelta(seconds=(3600*5)) + datetime.timedelta(seconds= time)
    embed = discord.Embed(
        title=f"React with 🎉 to win **{prize}**!\nTime remaining:  **{timeRemaning(time)}**",
        description="",
        color=0x006400
    )
    embed.set_author(name=f'{prize}', icon_url='')   # can't bold text
    embed.add_field(
        name=f"Hosted by:",
        value=ctx.author.mention
    )
    # embed.set_footer(text=f"Giveaway started at {time}\n CST") # , value=f"{end} from now!")      giveaway kończy sie za X czasu
    await ctx.send(file=discord.File('./imgs/giveaway.png'))

    my_msg = await channel.send(embed = embed)
    giveaway_messageId = giveway_idFunction(my_msg.id)

    await my_msg.add_reaction("🎉")
    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won {prize}.\nYou have 24h to contact KingStix to get ur {prize}")
    return giveaway_messageId

    # REROLL
@client.command()
@commands.has_permissions(administrator=True)
async def reroll(ctx, channel : discord.TextChannel):
    print(giveway_idFunction.ids)
    try:
        new_msg = await channel.fetch_message(giveway_idFunction.ids)
    except:
        print(giveway_idFunction.ids)
        await ctx.send("The id was entered incorrectly")
        return
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)
    await channel.send(f"Congratulations! New winner of {prize} is {winner.mention}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def prune(ctx, amount=7):
    await ctx.channel.purge(limit=amount)













    # ERROR HANDLING

@client.event
async def on_command_error(ctx, error):
    print(ctx.command.name + " was not used correctly")
    print(error)


client.run(os.environ['TOKEN'])