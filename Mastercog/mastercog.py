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
    async def noshow(self, ctx):
        """This does stuff!"""
        await ctx.send("It's currently",time.strftime("%I:$M") ,"and we're all still waiting..")