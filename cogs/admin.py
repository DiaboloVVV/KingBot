import discord
import datetime
from dateutil import tz
import asyncio
import random
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from normalFunctions import *
import os


class administrator(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x1D474C

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('with ravens..'))
        print('Has been logged in as {0.user}'.format(self.client))

    # testing purpose
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rules(self, ctx):
        channel = self.client.get_channel(835169449166372914)
        file = discord.File("./imgs/rulesleft.png", filename="rulesleft.png")
        e = discord.Embed(title='', description='', color=self.color)
        e.set_image(url='attachment://rulesleft.png')
        await channel.send(file=file, embed=e)
        e = discord.Embed(title='', description='', color=self.color)
        e.add_field(name='**1.) Discord ToS.**',value="This goes without saying, if you've been seen breaking discord"
        "ToS you will be punished depending on the severity of the situation.",inline=False)
        e.add_field(name='**2.) No NSFW content.**',value='NSFW content will not be tolerated no matter the situation ',inline=False)
        e.add_field(name='**3.) Respect KingStix and Staff.**',value='Any disrespect and toxicity towards KingStix and his Staff members'
                                                       'will result in punishment',inline=False)
        e.add_field(name='**4.) Respect other members of the server.**',value=' Be nice to others/No harassment/Bullying.',inline=False)
        e.add_field(name='**5.) No Spamming.**',value='This goes without saying, any spamming, flooding chat with CAPS '
                                                  'will be punished.',inline=False)
        e.add_field(name='**6.) No advertising**',value='Advertising without permission from Moderators will result in punishment.',inline=False)
        e.add_field(name='**7.) Use your common sense.**',value='Use your common sense "oh, but that wasn\'t specifically stated in the rules!'
                            ' Yeah, well it was probably stupid and you\'re going to get punished for it. Use your common sense before doing something.'
                            ' If you\'re not sure, and want to avoid getting in trouble, ask a Moderator.', inline=False)
        await channel.send(embed=e)
        e = discord.Embed(title='', description='', color=self.color)
        e.add_field(name='**React with <:KingStix:495646970384351242>  to Access The Server**',value="By accessing to the server you are automatically accepting the rules and becoming a member.")
        await channel.send(embed=e)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx):
        file = discord.File("./imgs/rolesleft.png", filename="rolesleft.png")
        e = discord.Embed(title='', description='', color=self.color)
        e.set_image(url='attachment://rolesleft.png')
        # e.set_image(url='https://im6.ezgif.com/tmp/ezgif-6-05670fead996.gif')   # here will be roles banner not rulesX2
        await ctx.channel.send(file=file, embed=e)
        levels = {
            'le50': 835204904200699957,
            'le40': 833879990801399889,
            'le30': 833879701855404059,
            'le20': 833879416811552778,
            'le10': 833879292760686602,
            'le5':  833879048539209768
        }
        le50 = get(ctx.guild.roles, id=levels["le50"])
        le40 = get(ctx.guild.roles, id=levels["le40"])
        le30 = get(ctx.guild.roles, id=levels["le30"])
        le20 = get(ctx.guild.roles, id=levels["le20"])
        le10 = get(ctx.guild.roles, id=levels["le10"])
        le5 = get(ctx.guild.roles, id=levels["le5"])


        e = discord.Embed(title='**<:GASM:774420336049389609> You can get diffrent color by being active on the server. <:EVEWAVE:774420313454805012>**', description=
                    'Every minute that you\'re messaging, you randomly gain between 15 and 25 XP.'
                    '__To avoid spamming__, earning XP is limited to __once a minute per user__.'
                    f'In the server, you type !rank in {self.client.get_channel(438749366623141889).mention} to see your rank and level.\n'
                    f'~ Level 5  ~  {le5.mention} \n'
                    f'~ Level 10 ~ {le10.mention} \n'
                    f'~ Level 20 ~ {le20.mention} \n'
                    f'~ Level 30 ~ {le30.mention} \n'
                    f'~ Level 40 ~ {le40.mention} \n'
                    f'~ Level 50 ~ {le50.mention}\n'
                    f'When you are **RANK 1** on the server leaderboard, you\'ll get {get(ctx.guild.roles, id=458991750590103571).mention} with color of yours.',
                          color=self.color)
        await ctx.channel.send(embed=e)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def roles2(self, ctx):
        e = discord.Embed(title='**<:GASM:774420336049389609> Assign Region&Position roles <:EVEYUMMI:774420328763490335>**', description='We mostly talk about **League Of Legends**.'
        ' So in order to find someone to play with, you can **choose region** you are playing and **position** you are maining.', color=self.color)
        await ctx.channel.send(embed=e)
        e = discord.Embed(title='Choose your position!',
                          description=f'<:TOP:835223543839064131> *Top lane* »» {get(ctx.guild.roles, id=835239647650775131).mention} \n'
                                    f'<:MIDDLE:835223544148787240> *Mid lane* »» {get(ctx.guild.roles, id=835239919823618048).mention} \n'
                                    f'<:JUNGLE:835223544131485706> *Jungle* »»  {get(ctx.guild.roles, id=835240061725048872).mention}   \n'
                                    f'<:ADC:835223544148787200> *Bot lane* »» {get(ctx.guild.roles, id=835240181489336343).mention} \n'
                                    f'<:SUPPORT:835223543855054930> *Support* »» {get(ctx.guild.roles, id=835240288967983174).mention}  \n', color=self.color)
        msg_1 = await ctx.channel.send(embed=e)
        await msg_1.add_reaction('<:TOP:835223543839064131>')
        await msg_1.add_reaction('<:MIDDLE:835223544148787240>')
        await msg_1.add_reaction('<:JUNGLE:835223544131485706>')
        await msg_1.add_reaction('<:ADC:835223544148787200>')
        await msg_1.add_reaction('<:SUPPORT:835223543855054930>')

        region_roles = {
            'oce': 801573190551863326,
            'na': 801573295820374016,
            'kr': 801573424098181130,
            'jp': 801573572413882488,
            'euw': 801573600011485194,
            'eune': 801573768874950677,
            'br': 801573996335464458,
            'las': 801574146219180113,
            'lan': 801574191786491984,
            'ru': 801574249587671101,
            'tr': 801574292298661938,
            'gr': 801574443050336288
        }
        e = discord.Embed(title='Choose your region!', description=f"<:na:835282302908760094> North America »»{get(ctx.guild.roles, id=region_roles['na']).mention} \n"
                          f"<:euw:835282302703632475> Europe West »» {get(ctx.guild.roles, id=region_roles['euw']).mention} \n"
                          f"<:eune:835282302396792893> Europe Nordic & East »»  {get(ctx.guild.roles, id=region_roles['eune']).mention} \n"
                          f"<:tr:835282302543069205> Turkey »» {get(ctx.guild.roles, id=region_roles['tr']).mention} \n"
                          f"<:jp:835282302484611133> Japan »» {get(ctx.guild.roles, id=region_roles['jp']).mention} \n"
                          f"<:kr:835282302560370813> Republic of Korea »» {get(ctx.guild.roles, id=region_roles['kr']).mention} \n"
                          f"<:oce:835282302899716146> Oceania »» {get(ctx.guild.roles, id=region_roles['oce']).mention} \n"
                          f"<:br:835282302447124491> Brazil »» {get(ctx.guild.roles, id=region_roles['br']).mention} \n"
                          f"<:gr:835282302841782312> Garena »» {get(ctx.guild.roles, id=region_roles['gr']).mention} \n"                                     
                          f"<:las:835282303118475264> Latin America South »» {get(ctx.guild.roles, id=region_roles['las']).mention} \n"
                          f"<:lan:835282302795644968> Latin America North »» {get(ctx.guild.roles, id=region_roles['lan']).mention} \n"      
                          f"<:ru:835282302967087124> Russia »» {get(ctx.guild.roles, id=region_roles['ru']).mention} \n", color = self.color)

        msg_1 = await ctx.channel.send(embed=e)

        # e = discord.Embed(title="Giveaway&Twitch Notification", description="")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mess(self, ctx):
        e = discord.Embed(title="Stream SURVEY", description="1) Steam will take place as planned. »» ✅\n"
        "2) Steam will be delayed. »» ❓\n"
        "3) Steam will not take place. »» ❌", color=self.color)
        msg = await ctx.channel.send(embed=e)

        await msg.add_reaction('✅')
        await msg.add_reaction('❓')
        await msg.add_reaction('❌')


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def prune(self, ctx, amount=7):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def gstart(self, ctx):
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
                msg = await self.client.wait_for('message', timeout=15.0, check=validation)
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

        channel = self.client.get_channel(channel_id)

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
        end = datetime.datetime.utcnow() - datetime.timedelta(seconds=(3600 * 5)) + datetime.timedelta(seconds=time)
        embed = discord.Embed(
            title=f"React with 🎉 to win **{prize}**!\nTime remaining:  **{timeRemaning(time)}**",
            description="",
            color=0x006400,
        )
        embed.set_author(name=f'{prize}', icon_url='')  # can't bold text
        embed.add_field(
            name=f"Hosted by:",
            value=ctx.author.mention
        )
        # embed.set_footer(text=f"Giveaway started at {time}\n CST") # , value=f"{end} from now!")      giveaway kończy sie za X czasu

        file = discord.File("./imgs/Giveaway.png", filename="Giveaway.png")
        e = discord.Embed(title='',description='',color=0x006400)
        e.set_image(url='attachment://Giveaway.png')
        await channel.send(file=file, embed=e)
        my_msg = await channel.send(embed=embed)
        giveaway_messageId = giveway_idFunction(my_msg.id)

        await my_msg.add_reaction("🎉")
        await asyncio.sleep(time)

        new_msg = await channel.fetch_message(my_msg.id)
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)

        await channel.send(
            f"Congratulations! {winner.mention} won {prize}.\nYou have 24h to contact KingStix to get ur {prize}")
        return giveaway_messageId

        # REROLL

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reroll(self, ctx, channel: discord.TextChannel):
        print(giveway_idFunction.ids)
        try:
            new_msg = await channel.fetch_message(giveway_idFunction.ids)
        except:
            print(giveway_idFunction.ids)
            await ctx.send("The id was entered incorrectly")
            return
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winner = random.choice(users)
        await channel.send(f"Congratulations! New winner of {prize} is {winner.mention}")


def setup(client):
    client.add_cog(administrator(client))