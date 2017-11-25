import discord
import os
import asyncio

from discord.ext import commands
from cogs import Player

class Start:
    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    def read_integers(self, filename):
        with open(filename) as f:
            return [int(x) for x in f]

  #  async def __local_check(self, ctx):
#        return ctx.command.name == 'classes'

    async def newPlayerEvent(self, ctx):
        await ctx.send(f'Welcome, {ctx.author.name}. TowerRPG is a text-based RTS MMORPG on Discord!')
        await asyncio.sleep(2)
        await ctx.send(f'{ctx.author.name}, please choose your class using the command !classchoose <id>. To read more about each class, do !classes')
        #somehow activates something in a check

    async def hasNotChosenClass(ctx):
        player = self.players.get(ctx.author.id)
        return player.getClassId() == 0

    @commands.command(name='classchoose')
    @commands.check(hasNotChosenClass)
    async def classChooseEvent(self, ctx, arg1):
        
        
        def check(m):
            if m.content != '!classes':
                classCho
            return m.content == '!classes'
        msg = await self.bot.wait_for('message', check=check)
        print(msg.content)

    @commands.command(name='register')
    async def register(self, ctx):
        if await self.getPlayer(ctx):
            await ctx.send(f'{ctx.author.name}, you are already logged in!')
        else:
            if os.path.isfile(f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.txt'):
                await ctx.send(f'{ctx.author.name}, you have already registered before, please do !login instead.')
            else:
                f = open(f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.txt', 'w+')
                f.close()
                player = Player(True, None, ctx.author.id)

                self.players.update({ctx.author.id:player}) #key:value

                await ctx.send(f'{ctx.author.name}, you have sucessfully registered.')
  

                await self.newPlayerEvent(ctx)

    @commands.command(name='login')
    async def login(self, ctx):
        if await self.getPlayer(ctx):
            await ctx.send(f'{ctx.author.name}, you are already logged in!')
        else:
            filepath = f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.txt'
            if os.path.isfile(filepath):
                c = self.read_integers(filepath)
                player = Player(False, c, ctx.author.id)

                self.players.update({ctx.author.id:player}) #key:value
                await ctx.send(f'{ctx.author.name}, you have successfully logged in. Welcome back!')
            else:
                await ctx.send(f'{ctx.author.name}, you haven\'t registed yet, please do !register.')

    async def getPlayer(self, ctx):
        return ctx.author.id in self.players
        
def setup(bot):
    bot.add_cog(Start(bot))
