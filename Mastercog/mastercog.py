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
            "NoShowResponses": ["{user} it's {current_time} and we're all still waiting..."]    
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
    async def noshow_add(self, ctx, response: str = None):
        """Adds response to list"""
        async with self.config.NoShowResponses() as responses:
            if response in responses:
                responses.remove(response)
                await ctx.send("Response removed")
            else:
                responses.append(response)
                await ctx.send("Response added")              

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

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        channel = message.channel
        if message.author == self.bot.user:
            return        
        if "1223" in message.content:
           await channel.send("Listner worked?")