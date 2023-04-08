import discord
import random
import time
from redbot.core import commands
from redbot.core import Config

class MasterCog(commands.Cog):
    """Testing cog to learn Python"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=467964879448)

        default_global = {
            "Members": [],
            "NoShowResponses": ["{user} it's {current_time} and we're all still waiting..."],
            "WallaceResponses" : ["That went as well as could be expected, didn't it?"]    
        }

        self.config.register_global(**default_global)

    @commands.command()
    async def noshow(self, ctx, user):
        """Calls out people who say they will be on at a certain time"""
        msg = random.choice(await self.config.NoShowResponses())
        current_time=time.strftime("%I:%M")
        if "{user}" in msg and "{current_time}" in msg:
            await ctx.send(msg.format(user=user, current_time=current_time))
        else:
            await ctx.send(msg)                       

    @commands.command()
    @commands.is_owner()
    async def user_add(self, ctx, member):
        """Adds response to list"""
        async with self.config.Members() as members:
            if member in members:
                members.remove(member)
                await ctx.send("User removed")
            else:
                members.append(member)
                await ctx.send("User added")


    # @commands.command()
    # @commands.is_owner()
    # async def ready(self, ctx):
    #     """Checks whos available"""
    #     members = await self.config.Members()
    #     for member in members:
    #         user = await discord.client.fetch_user()
    #         await user.send("Hello there!")             
                 
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        wallace_triggers = ["cheese", "wallace", "gromit", "🧀", "audiobook", "wensleydale", "trousers", "moon", "mutt"]
        channel = message.channel
        chance = random.randint(0, 100)
        msg = message.content.lower()
        if message.author == self.bot.user:
            return
        elif "mitch" in msg and "chances" in msg:
            if message.author == "<@188811391610650624>":
                await channel.send("100% chance that you will be online. dont ask again.".format(chance))
                return
            else:
                await channel.send("{}% chance that <@188811391610650624> will be online".format(chance))
                return
        elif "mitch" in msg and "chance" in msg:
            await channel.send("{}% chance that <@188811391610650624> will be online".format(chance))
            return             
        for trigger in wallace_triggers:           
            if trigger in msg:
                response = random.choice(await self.config.WallaceResponses())
                await channel.send(response)
                break 

            
    # @commands.command()
    # async def mitch_chance(self, ctx, low = 0, high = 100):
    #     """Calculates chances mitch will be online tonight"""
    #     chance = random.randint(low, high)
    #     await ctx.send("Calculation complete. {}% chance that <@188811391610650624> will be on tonight".format(chance))

            