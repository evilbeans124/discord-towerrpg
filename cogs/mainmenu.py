import discord
import asyncio
import random
import numpy as np

from discord.ext import commands

class MainMenu:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='map')
    async def displayMap(self, ctx):
        start_cog = self.bot.get_cog('Start')
        player = await start_cog.getPlayer(ctx)

        x_position = player.getXPos()
        y_position = player.getYPos()
        board = [['.'] * 10 for _ in range(10)]
        board[x_position][y_position] = 'x'
        
        await ctx.send(f'```\n' +
                       f'{self.convertMap(board)}\n' +
                       f'```')

    def convertMap(self, board):
        string = ''
        for row in board:
            for val in row:
                string += '{:6}'.format(val)
            string += '\n'
        return string

    @commands.command(name='stats')
    async def displayStats(self, ctx):
        start_cog = self.bot.get_cog('Start')
        player = await start_cog.getPlayer(ctx)
        await ctx.send(f'```{ctx.author.name}\'s Stats ' +
                       f'\nHP: {player.getCurrentHp()}/{player.getMaxHp()}' +
                       f'\nMP: {player.getCurrentMp()}/{player.getMaxMp()}' +
                       f'\nLevel: {player.getLevel()} ({player.getExp()}/{player.getExpToLevel()}) ' +
                       f'\nGold: {player.getGold()}' +
                       f'\nFor more details about your attributes, do !attributes' +
                       f'```')

    @commands.command(name='attributes')
    async def displayAttributes(self, ctx):
        start_cog = self.bot.get_cog('Start')
        player = await start_cog.getPlayer(ctx)
        await ctx.send(f'hi')

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
