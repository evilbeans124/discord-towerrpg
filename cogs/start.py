import discord
from discord.ext import commands

class Start:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='!register')
    async def checkRegister(self, ctx):
        

    def setup(bot):
        bot.add_cog(Start(bot))
