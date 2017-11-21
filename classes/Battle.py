import discord
import asyncio
import os

from classes.Player import Player
from classes.Mob import Mob
from classes.BoarClass import BoarClass
from classes.NumbersHandler import NumbersHandler

class Battle:
    whosTurn = None
    battler1 = None
    battler2 = None
    damage = None
    message = None
    client = None
    currentRound = None

    #Boarclass is supposed to be Mob
    def __init__(self, battler1, battler2, message, client):
        self.battler1 = battler1
        self.battler2 = battler2
        self.message = message
        self.client = client
        self.damage = 0
        self.currentRound = 1
        if isinstance(battler1, Player) and isinstance(battler2, BoarClass):
            asyncio.ensure_future(self.initiatePvEBattle())

    async def printBattleLog(self):
        await self.client.send_message(self.message.channel, "```==========" + self.message.author.name + " VS " + self.battler2.getName()
                                       +"==========\n\n" + self.message.author.name + "'s HP: " + str(self.battler1.getCurrentHp())
                                       + "/" + str(self.battler1.getMaxHp()) + "\n" + self.message.author.name + "'s MP: "
                                       + str(self.battler1.getCurrentMp()) + "/" + str(self.battler1.getMaxMp()) + "\n\n" + self.battler2.getName()
                                       + "'s HP: " + str(self.battler2.getCurrentHp()) + "/" + str(self.battler2.getMaxHp()) + "\n"
                                       + self.battler2.getName() + "'s MP: " + str(self.battler2.getCurrentMp()) + "/" + str(self.battler2.getMaxMp()) + "```")

    def determineWhoFirst(self):
        if self.battler1.getSpeed() > self.battler2.getSpeed():
            self.whosTurn = self.battler1
        elif self.battler1.getSpeed() < self.battler2.getSpeed():
            self.whosTurn = self.battler2
        else:
            if random.randint(1, 2) == 1:
                self.whosTurn = self.battler1
            else:
                self.whosTurn = self.battler2

    async def playerAction(self):
        await self.client.send_message(self.message.channel, "It's " + self.message.author.name + "'s turn.")
        await self.client.send_message(self.message.channel, "Available commands: !attack, !skill <id>, !items <id>, !run")
        returnCommand = client.wait_for_message(author=self.message.author)
        if returnCommand.content.startswith('!attack'):
            playerAttack()
        else:
            await self.client.send_message(self.message.channel, "Invalid command. Please try again.")

    async def playerAttack(self):
        return None

    async def mobAttack(self):
        await self.client.send_message(self.message.channel, "It's " + self.battler2.getName() + "'s turn.")
        await asyncio.sleep(1.25)

        #action = battler2.getAction()
        #damage = int(battler2.getDamage())

        action = self.getAction(self.battler2)
        
        await self.client.send_message(self.message.channel, action)
        self.battler1.decrease_hp(self.damage)

        self.whosTurn = self.battler1

    async def mobGetAction(self, actioner):
        if random.randint(1, 4) == -1: #execute a skill
            #skill = xxx
            #getSkillName = random.randint(0, len(Skills.getAllSkills))
            #getSkillDamage = 
            
            #return self.name " uses " + getSkillName + ". Dealt "
            return None
        else: #execute a regular attack
            self.damage = math.floor(self.attack * 1.5)
            return self.name + " uses normal attack. Dealt " + self.damage + " damage."

    async def initiatePvEBattle(self):
        #battler1 is player, battler2 is mob
        self.printBattleLog()
        self.determineWhoFirst()

        while self.battler1.getCurrentHp() > 0 and self.battler2.getCurrentHp() > 0:
            self.printBattleLog()
            if isinstance(whosTurn, Player):
                await self.playerAction()
            else:
                await self.mobAttack()

        await self.client.send_message(self.message.channel, "The battle has ended!")
