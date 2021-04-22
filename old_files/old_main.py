import discord
import datetime
import asyncio
import random
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os

    # GLOBAL VARIABLES
# TOKEN=os.environ['TOKEN']
prefix = '$'
client = commands.Bot(command_prefix=prefix)

    # DISPLAYING WHEN BOT IS READY TO GO
@client.event
async def on_ready():
    print('Has been logged in as {0.user}'.format(client))

    # YOU CAN TEST IF IT WORKS
@client.command()
async def work(message):
    mess = await message.channel.send('Love you!')
    # await asyncio.sleep(0.5)
    # await mess.edit(content='Emm- hello!')


    # GETTING MENTIONED USER AVATAR
@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)



def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s":1, "m":60, "h" : 3600, "d":3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


    # CREATING GIVEWAY
@client.command()
@commands.has_permissions(administrator=True)
async def gstart(ctx, mins : int, *, prize: str):
    # await ctx.send("<:OpChad:774420354553741344> ** GIVEAWAY ** <:OpChad:774420354553741344>")
    await ctx.send(file=discord.File('./imgs/test.png'))
    embed = discord.Embed(
        title = f"{prize}",
        description= "React with 🎉 to join!",
        color= 0x006400
    )
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds= mins)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.add_field(name = "Ends At:", value = f"{end} UTC")
    # embed.set_footer(text = f"Ends {mins} minutes from now!")

    my_msg = await ctx.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins)

    new_msg = await ctx.channel.fetch_message(my_msg.id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congrats {winner.mention} won {prize}!")
    return await ctx.channel.fetch_message(my_msg.id)


    # ERROR HANDLING
@client.event
async def on_command_error(ctx, error):
    print(ctx.command.name + " was not used correctly")
    print(error)


    # LAUNCHING BOT
client.run(os.environ['TOKEN'])
