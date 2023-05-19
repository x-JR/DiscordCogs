import discord
from redbot.core import commands
import asyncio

answers = {}

class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Online', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is green.', ephemeral=True)

    @discord.ui.button(label='Unsure', style=discord.ButtonStyle.red, custom_id='persistent_view:grey')
    async def grey(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is grey.', ephemeral=True)

    @discord.ui.button(label='Unavailable', style=discord.ButtonStyle.grey, custom_id='persistent_view:red')
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is red.', ephemeral=True)        

class ReadyChecker(commands.Cog):
    """Checks which boys are ready tonight"""
    def __init__(self, bot):
        self.bot = bot
    async def setup_hook(self) -> None:
        self.add_view(PersistentView())    
            
    @commands.command(description="Check if your homies are ready")
    async def rc(self, ctx: commands.Context):
        """Check if your homies are ready"""
        await ctx.send('Ready-Check for Tonight:', view=PersistentView())

    @commands.command(description="Check if your homies are ready")
    async def status(self, ctx: commands.Context):
        """Check if your homies are ready / Global Test"""
        users = list(answers.keys())
        status = list(answers.values())
        message = ""
        empty = "No Responses Yet :("
        if users is None:
            await ctx.send(f"Status Tonight: \n{empty}") 
        else:    
            for i in range (0, len(users)):
                message = message + (f"> {users[i]} : {status[i]} \n")
            await ctx.send(f"Status Tonight: \n{message}")        