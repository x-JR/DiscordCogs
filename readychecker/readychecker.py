import discord
from redbot.core import commands
import asyncio

answers = {}

class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Online', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Marked as available.', ephemeral=True)
        answers[str(interaction.user)] = "Online 🟢"    

    @discord.ui.button(label='Unsure', style=discord.ButtonStyle.grey, custom_id='persistent_view:grey')
    async def grey(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Marked as Unsure.', ephemeral=True)
        answers[str(interaction.user)] = "Unsure 🤷‍♀️"    

    @discord.ui.button(label='Unavailable', style=discord.ButtonStyle.red, custom_id='persistent_view:red')
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Marked as unavailable tonight.', ephemeral=True) 
        answers[str(interaction.user)] = "Unavailable 🔴"

    @discord.ui.button(label='Whos Available?', style=discord.ButtonStyle.primary, custom_id='persistent_view:check')
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        users = list(answers.keys())
        status = list(answers.values())
        message = ""
        if users is None:
            message = "No Responses Yet."
        else:    
            for i in range (0, len(users)):
                message = message + (f"> {status[i]} : {users[i]} \n")
        await interaction.response.send_message(f"Status Tonight: \n{message}", ephemeral=True)           

class ReadyChecker(commands.Cog):
    """Checks which boys are ready tonight"""
    def __init__(self, bot):
        self.bot = bot
    async def setup_hook(self) -> None:
        self.add_view(PersistentView())    
            
    @commands.command(description="Check if your homies are ready")
    async def rc(self, ctx: commands.Context):
        """Check if your homies are ready"""
        answers.clear 
        await ctx.send('Will you be on today?:', view=PersistentView())

    @commands.command(description="Check if your homies are ready")
    async def status(self, ctx: commands.Context):
        """Check if your homies are ready / Global Test"""
        users = list(answers.keys())
        status = list(answers.values())
        message = ""
        empty = "No Responses Yet."
        if users is None:
            await ctx.send(f"Status Tonight: \n{empty}") 
        else:    
            for i in range (0, len(users)):
                message = message + (f"> {status[i]} : {users[i]} \n")
            await ctx.send(f"Status Tonight: \n{message}")        