import discord
import os
import asyncio

from discord.ext import commands
from cogs.Player import Player

class Start:    
    def __init__(self, bot):
        self.bot = bot
        self.players = {}
        self.playerState = {}

    def read_integers(self, filename):
        with open(filename) as f:
            return [int(x) for x in f]

    async def newPlayerEvent(self, ctx):
        await ctx.send(f'Welcome, {ctx.author.name}. TowerRPG is a text-based RTS MMORPG on Discord!')
        await asyncio.sleep(1.5)
        await ctx.send(f'{ctx.author.name}, please choose your class using the command !classchoose <id>. To read more about each class, do !classes')

    async def hasNotChosenClass(self, ctx):
        player = self.players.get(ctx.author.id)
        return player.getClassId() == 0

    @commands.command(name='classchoose')
    async def classChooseEvent(self, ctx, arg1):
        if (not type(arg1)) == int and (not arg1.is_integer()):
            ctx.send(f'{ctx.author.name}, you have inputted a wrong class id. Try again.')
        else:
            class_id = int(arg1)
            player = self.players.get(ctx.author.id)
            player.setClass(class_id)
            self.players.update({ctx.author.id:player}) #key:value
            self.playerState.update({ctx.author.id:'main_menu'})
            await ctx.send(f'{ctx.author.name}, you have successfully chose {player.getClass().getClassName()} as your class!')

    @commands.command(name='classes')
    async def listClassesEvent(self, ctx):
        await ctx.send(f'SOMETHING LOL')

    @commands.command(name='register')
    async def register(self, ctx):
        if await self.getIsPlayer(ctx):
            await ctx.send(f'{ctx.author.name}, you are already logged in!')
        else:
            if os.path.isfile(f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.txt'):
                await ctx.send(f'{ctx.author.name}, you have already registered before, please do !login instead.')
            else:
                f = open(f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.txt', 'w+')
                f.close()
                player = Player(True, None, ctx.author.id)

                self.players.update({ctx.author.id:player}) #key:value
                self.playerState.update({ctx.author.id:"class_choose"})

                await ctx.send(f'{ctx.author.name}, you have sucessfully registered.')
  
                await self.newPlayerEvent(ctx)

    @commands.command(name='login')
    async def login(self, ctx):
        if await self.getIsPlayer(ctx):
            await ctx.send(f'{ctx.author.name}, you are already logged in!')
        else:
            filepath = f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.txt'
            if os.path.isfile(filepath):
                c = self.read_integers(filepath)
                player = Player(False, c, ctx.author.id)

                self.players.update({ctx.author.id:player}) #key:value
                self.playerState.update({ctx.author.id:"main_menu"})
                await ctx.send(f'{ctx.author.name}, you have successfully logged in. Welcome back!')
            else:
                await ctx.send(f'{ctx.author.name}, you haven\'t registed yet, please do !register.')

    async def getIsPlayer(self, ctx):
        return ctx.author.id in self.players

    #the below two go together :3
    async def getPlayer(self, ctx):
        return self.players.get(ctx.author.id)

    async def updatePlayer(self, ctx, thePlayer):
        self.players.update({ctx.author.id:thePlayer}) #key:value

    #stuff about a player's state. state is a string.
    async def getPlayerState(self, ctx):
        return self.playerState.get(ctx.author.id)

    async def updatePlayerState(self, ctx, state):
        self.playerState.update({ctx.author.id:state}) #key:value
        
def setup(bot):
    bot.add_cog(Start(bot))
