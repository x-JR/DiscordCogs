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
            "Members": {},
            "NoShowResponses": ["{user} it's {current_time} and we're all still waiting..."]    
        }

        self.config.register_guild(**default_global)

    @commands.command()
    async def noshow(self, ctx, user):
        """Calls out people who say they will be on at a certain time"""
        current_time = time.strftime("%I:%M")
        await ctx.send(f"{user} it's {current_time} and we're all still waiting...")

    @commands.command()
    async def Test2(self, ctx,):
        """Test Command"""
        msg = random.choice(await self.config.NoShowResponses())
        await ctx.send(f"{msg}")        

    @commands.command()
    async def Check(self, ctx,):
        """Test Command"""
        msg = await self.config.NoShowResponses()
        await ctx.send(f"{msg}")                