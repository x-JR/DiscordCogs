import discord
from redbot.core import commands
import random

class MasterCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")