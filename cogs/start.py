import discord
import os
import asyncio

import io
import json

from discord.ext import commands
from cogs.Player import Player
from cogs.Classes import Classes

from cogs.Mob import Mob

class Start:    
    def __init__(self, bot):
        self.bot = bot
        self.players = {}
        self.playerState = {}
        
    async def newPlayerEvent(self, ctx):
        await ctx.send(f'Welcome, {ctx.author.name}. TowerRPG is a text-based RTS MMORPG on Discord!')
        await asyncio.sleep(1.5)
        await ctx.send(f'{ctx.author.name}, please choose your class using the command !classchoose <id>. To read more about each class, do !classes')

    async def hasNotChosenClass(self, ctx):
        player = self.players.get(ctx.author.id)
        return player.getClassId() == 0

    @commands.command(name='classchoose')
    async def classChooseEvent(self, ctx, arg1):
        def check_int(s):
            if s[0] in ('-', '+'):
                return s[1:].isdigit()
            return s.isdigit()

        if (not check_int(arg1) or int(arg1) < 1 or int(arg1) > len(Classes.getAllClasses()) - 1):
            await ctx.send(f'{ctx.author.name}, you have inputted a wrong class id. Try again.')
        else:
            class_id = int(arg1)
            player = self.players.get(ctx.author.id)
            player.setClass(class_id)
            self.players.update({ctx.author.id:player}) #key:value
            self.playerState.update({ctx.author.id:'main_menu'})
            await ctx.send(f'{ctx.author.name}, you have successfully chose {player.getClass().getClassName()} as your class!')

    @commands.command(name='classes')
    async def listClassesEvent(self, ctx):
        await ctx.send(f'```ID    Name        Description\n\n' +
                       f'1     Warrior     Tank and melee\n' +
                       f'2     Ranger      Archer, Gunslinger, etc...\n' +
                       f'3     Mage        Magic user class\n' +
                       f'```')

    @commands.command(name='register')
    async def register(self, ctx):
        if await self.getIsPlayer(ctx):
            await ctx.send(f'{ctx.author.name}, you are already logged in!')
        else:
            if os.path.isfile(f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.json'):
                await ctx.send(f'{ctx.author.name}, you have already registered before, please do !login instead.')
            else:
                await self.createPlayerFile(ctx)
                
                player = Player(ctx.author.id)

                self.players.update({ctx.author.id:player}) #key:value
                self.playerState.update({ctx.author.id:"class_choose"})

                await ctx.send(f'{ctx.author.name}, you have sucessfully registered.')
  
                await self.newPlayerEvent(ctx)

    @commands.command(name='login')
    async def login(self, ctx):
        if await self.getIsPlayer(ctx):
            await ctx.send(f'{ctx.author.name}, you are already logged in!')
        else:
            filepath = f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.json'
            if os.path.isfile(filepath):
                player = Player(ctx.author.id)

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

    async def createPlayerFile(self, ctx):        
        f = open(f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{ctx.author.id}.json', 'w+')
        f.close()
        
        filepath = f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{str(ctx.author.id)}'
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str

        data = {'attributes': {'strength': 5,
                               'dexterity': 5,
                               'intellect': 5,
                               'hp_regen': 0,
                               'mp_regen': 0,
                               'spell_power': 5,#not true though, edit based on class
                               'attack_power': 5,
                               'physical_defense': 0,
                               'magical_defense': 0,
                               'speed': 5,
                               'accuracy': 95,
                               'parry_chance': 0,
                               'critical_chance': 2.5,
                               'critical_damage_multiplier': 2,
                               'block_chance': 0,
                               'dodge_chance': 0},
                'statistics': {'current_hp': 50,
                               'max_hp': 50,
                               'current_mp': 10,
                               'max_mp': 10,
                               'level': 1,
                               'experience': 0,
                               'experienceToLevel': 100,
                               'gold': 100,
                               'current_tower_level': 1},
                'personal_no_display': {'class_id': 0,
                               'message_author_id': ctx.author.id,
                               'coordinates': [5, 5]}}

        with io.open(f'{filepath}.json', 'w+', encoding='utf8') as outfile:
            str_ = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))
        
def setup(bot):
    bot.add_cog(Start(bot))
