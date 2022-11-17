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
            "Members": None,     
        }

        self.config.register_guild(**default_guild)

    @commands.command()
    async def noshow(self, ctx, arg1):
        """This does stuff!"""
        time = time.strftime("%I:%M")"
        await ctx.send("{arg1} it's {time} and we'll all still waiting...")