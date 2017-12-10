import discord
import asyncio

from discord.ext import commands
from cogs.PvEBattle import PvEBattle
from cogs.Mob import Mob

class PvEBattleInterface:
    def __init__(self, bot):
        self.bot = bot
        #value is battle object, key is ctx.author.id
        self.currentPvEBattles = {}

    async def __local_check(self, ctx):
        battle = self.currentPvEBattles.get(ctx.author.id)
        return isinstance(battle.getCurrentTurn(), type(battle.getPlayer()))

    async def initiatePvEBattle(self, ctx):
        start_cog = self.bot.get_cog('Start')
        player = await start_cog.getPlayer(ctx)
        mob = Mob.encounterRandomMob(player)
        PvEbattle = PvEBattle(player, mob)
        self.currentPvEBattles.update({ctx.author.id:PvEbattle}) #key:value
        await ctx.send(f'{ctx.author.name}, you have encountered a {mob.getName()}. Battle begins!')

        await self.printBattleLog(ctx, mob, player)

        if isinstance(PvEbattle.getCurrentTurn(), type(PvEbattle.getMob())):
            await self.mobTurn(ctx)
        elif isinstance(PvEbattle.getCurrentTurn(), type(PvEbattle.getPlayer())):
            await self.playerTurn(ctx)

    @commands.command(name='attack')
    async def attack(self, ctx):
        battle = self.currentPvEBattles.get(ctx.author.id)
        dmg = battle.playerAttack()
        self.currentPvEBattles.update({ctx.author.id:battle})
        await ctx.send(f'{ctx.author.name} uses normal attack. Dealt {dmg} damage.')
        await self.endOfTurn(ctx)

    #not done yet
    @commands.command(name='skill')
    async def skill(self, ctx):
        battle = self.currentPvEBattles.get(ctx.author.id)
        await ctx.send(f'skill')
        
        await self.endOfTurn(ctx)

    #not done yet
    @commands.command(name='items')
    async def items(self, ctx):
        battle = self.currentPvEBattles.get(ctx.author.id)
        await ctx.send(f'items')
        
        await self.endOfTurn(ctx)

    #not done yet
    @commands.command(name='run')
    async def run(self, ctx):
        battle = self.currentPvEBattles.get(ctx.author.id)
        await ctx.send(f'run')
        
        await self.endOfTurn(ctx)

    async def playerTurn(self, ctx):
        await ctx.send(f'It\'s {ctx.author.name}\'s turn.')
        await asyncio.sleep(1)
        await ctx.send(f'Available commands: !attack, !skill <id>, !items <id>, !run')

    async def mobTurn(self, ctx):
        battle = self.currentPvEBattles.get(ctx.author.id)
        await ctx.send(f'It\'s {battle.getMob().getName()}\'s turn.')
        await asyncio.sleep(1)
        
        actionString = battle.mobAction()
        if actionString == 'skill':
            battle.mobSkill()
        elif actionString == 'attack':
            dmg = battle.mobAttack()
            await ctx.send(f'{battle.getMob().getName()} uses normal attack. Dealt {dmg} damage.')
        await self.endOfTurn(ctx)

    async def printBattleLog(self, ctx, mob, player):
        await ctx.send(f'```========== {ctx.author.name} VS {mob.getName()} ==========' +
                       f'\n\n{ctx.author.name}\'s HP: {player.getCurrentHp()}/{player.getMaxHp()}' +
                       f'\n{ctx.author.name}\'s MP: {player.getCurrentMp()}/{player.getMaxMp()}' +
                       f'\n\n{mob.getName()}\'s HP: {mob.getCurrentHp()}/{mob.getMaxHp()}' +
                       f'\n{mob.getName()}\'s MP: {mob.getCurrentMp()}/{mob.getMaxMp()}```')

    async def endOfTurn(self, ctx):
        battle = self.currentPvEBattles.get(ctx.author.id)
        start_cog = self.bot.get_cog('Start')
        await start_cog.updatePlayer(ctx, battle.getPlayer())
        
        mob = battle.getMob()
        player = battle.getPlayer()
        await self.printBattleLog(ctx, mob, player)

        battleHasEnded = await self.checkBattleEnd(ctx, mob, player)

        if not battleHasEnded:
            battle.changeTurns()
            self.currentPvEBattles.update({ctx.author.id:battle})
            if isinstance(battle.getCurrentTurn(), type(battle.getPlayer())):
                await self.playerTurn(ctx)
            elif isinstance(battle.getCurrentTurn(), type(battle.getMob())):
                await self.mobTurn(ctx)

    async def checkBattleEnd(self, ctx, mob, player):
        start_cog = self.bot.get_cog('Start')
        if player.getCurrentHp() <= 0:
            await ctx.send(f'{ctx.author.name}, you have died!')
            await asyncio.sleep(1)
            await ctx.send(f'{ctx.author.name}, as punishment for your death, you lose 20% of your exp and gold.')
            player.decrease_gold(player.getGold() / 5)
            player.decrease_exp(player.getExp() / 5)
            player.setHp(player.getMaxHp())
            #update player
            await start_cog.updatePlayer(ctx, player)
            await start_cog.updatePlayerState(ctx, f'main_menu')
            return True

            #somehow end the damn thing
        elif mob.getCurrentHp() <= 0:
            await ctx.send(f'Congratulations! {ctx.author.name} has won the battle!')
            await asyncio.sleep(1)
            mobExp = mob.getExp()
            mobGold = mob.getGold()
            await ctx.send(f'{ctx.author.name}, you obtained {mobExp} exp and {mobGold} gold.')

            player.increase_exp(mobExp)
            player.increase_gold(mobGold)

            #update player
            await start_cog.updatePlayer(ctx, player)
            await start_cog.updatePlayerState(ctx, f'main_menu')
            return True

            #somehow end the damn thing
        else:
            return False

    async def endBattle(self, ctx):
        string = 'hi'

def setup(bot):
    bot.add_cog(PvEBattleInterface(bot))
