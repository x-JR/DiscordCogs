from .mastercog import MasterCog


def setup(bot):
    bot.add_cog(MasterCog(bot))