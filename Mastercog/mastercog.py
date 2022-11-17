import discord
import random
import time
from redbot.core import commands
from redbot.core import Config


class MasterCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=467964879446212608, force_registration=True)

        default_guild = {
            "Members": {},
            "NoShowResponses": ["{user} it's {current_time} and we're all still waiting..."]    
        }

        self.config.register_guild(**default_guild)

    @commands.command()
    async def noshow(self, ctx, user):
        """Calls out people who say they will be on at a certain time"""
        current_time = time.strftime("%I:%M")
        await ctx.send(f"{user} it's {current_time} and we're all still waiting...")

    @commands.command()
    async def Test2(self, ctx,):
        """Test Command"""
        msg = random.choice(await self.config.guild(ctx.guild).NoShowResponses())
        await ctx.send(f"{msg}")        