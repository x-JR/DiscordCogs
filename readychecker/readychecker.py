import discord
from redbot.core import commands
import asyncio

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Ready', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Adding to Ready List.', ephemeral=True)
        self.value = 'Ready'
        self.stop()

    @discord.ui.button(label='Tentative', style=discord.ButtonStyle.grey)
    async def tentative(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Marking as Tentative.', ephemeral=True)
        self.value = 'Tentative'
        self.stop()

    @discord.ui.button(label='Ignore', style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Ready Check Ignored.', ephemeral=True)
        self.value = 'Ignore'
        self.stop()        

class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Red', description='Your favourite colour is red', emoji='🟥'),
            discord.SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'),
            discord.SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦'),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f'Your favourite colour is {self.values[0]}')

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())



class ReadyChecker(commands.Cog):
    """Checks which homies are ready tonight"""
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command(description="Check if your homies are ready")
    async def readycheck(self, ctx: commands.Context):
        """Check if your homies are ready"""
        checklist = ['Jake_#1984', 'Cizomic#3549', 'Aus_Nate#2990', 'kazster#4356', 'Dingleberry#8464', 'Droid#7487', 'Spitfyre#7256']
        readyhomies = []
        counted = []
        tentative = []
        ignored = []
        dict = {}
        passes = 0
        message = await ctx.send("Initiating Ready Check")
        while len(counted) != len(checklist):
            for mem in ctx.guild.members:
                if mem.bot:
                    pass
                elif str(mem) not in checklist:
                    pass
                elif str(mem) not in counted:
                    passes += 1
                    if dict.get(str(mem), False) == False:
                        try:
                            view = Confirm()
                            readymsg = await mem.send("Will you be ready tonight?", view=view)
                            dict[str(mem)] = readymsg
                            await asyncio.sleep(30)
                            if view.value == 'Ready':
                                checklist.remove(str(mem))
                                readyhomies.append(str(mem.name))
                                counted.append(str(mem.name))
                                await readymsg.edit(content=f"Thank you for responding, I have informed {ctx.message.author.name}", view=None)
                            elif view.value == 'Tentative':
                                checklist.remove(str(mem))
                                tentative.append(str(mem.name))
                                counted.append(str(mem.name))
                                await readymsg.edit(content="Marked as tentative", view=None)
                            elif view.value == 'Ignore':
                                checklist.remove(str(mem))
                                ignored.append(str(mem.name))
                                counted.append(str(mem.name))
                                await readymsg.edit(content="Ignored", view=None)    

                        except discord.errors.Forbidden:
                            pass
                    else:
                        try:    
                            view = Confirm()
                            readymsg = dict.get(str(mem))
                            await asyncio.sleep(30)
                            if view.value == 'Ready':
                                readyhomies.append(str(mem.name))
                                await readymsg.edit(content=f"Thank you for responding, I have informed {ctx.message.author.name}", view=None)
                            elif view.value == 'Tentative':
                                tentative.append(str(mem.name))
                                await readymsg.edit(content="Marked as tentative", view=None)
                            elif view.value == 'Ignore':
                                ignored.append(str(mem.name))
                                await readymsg.edit(content="Ignored", view=None)

                        except discord.errors.Forbidden:
                            pass                    
                    await message.edit(content=f"Debug: Attempts:{passes}. Currently: {mem}, Replied: {counted}")
                elif passes < 18:
                    break
                else:
                    pass
        if readyhomies is None:
            await ctx.send(content=f"Nobody Replied :(")
        else:
            await ctx.send(content=f"On Tonight: {readyhomies} Undecided: {tentative} People who just ignored me: {checklist}")

    @commands.command(description="Check if your homies are ready")
    async def readycheck2(self, ctx: commands.Context):
        """Check if your homies are ready / Global Test"""
        view = DropdownView()
        await ctx.send('Pick your favourite colour:', view=view)