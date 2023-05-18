import discord
from redbot.core import commands
import asyncio

answers = {}

class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Available', description="You will be available tonight"),
            discord.SelectOption(label='Tentative', description="Not Certain"),
            discord.SelectOption(label='Unavailable', description='Unavailable Tonight'),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Will you be available tonight?', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Set Status for tonight to: {self.values[0]}", ephemeral=True)
        answers[str(interaction.user)] = str(self.values[0])

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())


class ReadyChecker(commands.Cog):
    """Checks which boys are ready tonight"""
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command(description="Check if your homies are ready")
    async def rc(self, ctx: commands.Context):
        """Check if your homies are ready"""
        view = DropdownView()
        await ctx.send('Ready-Check for Tonight:', view=view)

    @commands.command(description="Check if your homies are ready")
    async def status(self, ctx: commands.Context):
        """Check if your homies are ready / Global Test"""
        users = list(answers.keys())
        status = list(answers.values())
        message = ""
        empty = "No Responses Yet :("
        if answers is None:
            await ctx.send(f"Status Tonight: \n{empty}") 
        else:    
            for i in range (0, len(users)):
                message = message + (f"> {users[i]} : {status[i]} \n")
            await ctx.send(f"Status Tonight: \n{message}")        