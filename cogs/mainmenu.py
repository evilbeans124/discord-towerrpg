import discord
import asyncio
import random

from discord.ext import commands

class MainMenu:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stats')
    async def displayStats(self, ctx):
        await ctx.send(f'no, bad!')

    @commands.command(name='battle')
    async def lookForBattle(self, ctx):
        msg = await ctx.send(f'{ctx.author.name}, you are currently searching for a battle.')
        time = int(random.random() * 10)

        async def editDots(loop, time):
            end_time = loop.time() + time
            dots = f'{msg.content}.'
            while True:
                await msg.edit(content=str(dots))
                dots = f'{dots}.'
                if (loop.time() >= end_time):
                    break
                await asyncio.sleep(1)

        loop = asyncio.get_event_loop()
        await editDots(loop, time)
        
        start_cog = self.bot.get_cog('Start')
        await start_cog.updatePlayerState(ctx, 'in_battle')

        battle_cog = self.bot.get_cog('PvEBattleInterface')
        await battle_cog.initiatePvEBattle(ctx)

def setup(bot):
    bot.add_cog(MainMenu(bot))
