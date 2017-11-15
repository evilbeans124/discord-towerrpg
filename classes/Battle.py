import discord
import asyncio
import os

from classes.Player import Player
from classes.Mob import Mob
from classes.BoarClass import BoarClass

class Battle:
    whoFirst = None
    battler1 = None
    battler2 = None
    message = None
    client = None
    currentRound = None

    #Boarclass is supposed to be Mob
    def __init__(self, battler1, battler2, message, client):
        self.battler1 = battler1
        self.battler2 = battler2
        self.message = message
        self.client = client
        self.currentRound = 1
        if isinstance(battler1, Player) and isinstance(battler2, BoarClass):
            asyncio.ensure_future(self.initiatePvEBattle())

    async def printBattleLog(self):
        await self.client.send_message(self.message.channel, "```==========" + self.message.author.name + " VS " + self.battler2.getName()
                                       +"==========\n\n" + self.message.author.name + "'s HP: " + str(self.battler1.getCurrentHp())
                                       + "/" + str(self.battler1.getMaxHp()) + "\n" + self.message.author.name + "'s MP: "
                                       + str(self.battler1.getCurrentMp()) + "/" + str(self.battler1.getMaxMp()) + "\n\n" + self.battler2.getName()
                                       + "'s HP: " + str(self.battler2.getCurrentHp()) + "/" + str(self.battler2.getMaxHp()) + "\n"
                                       + self.battler2.getName() + "'s MP: " + str(self.battler2.getCurrentMp()) + "/" + str(self.battler2.getMaxMp())
                                       + "\n\nWhat will " + self.message.author.name + " do?```")

    def determineWhoFirst(self):
        if self.battler1.getSpeed() > self.battler2.getSpeed():
            self.whoFirst = self.battler1
        elif self.battler1.getSpeed() < self.battler2.getSpeed():
            self.whoFirst = self.battler2
        else:
            if random.randint(1, 2) == 1:
                self.whoFirst = self.battler1
            else:
                self.whoFirst = self.battler2

    async def mobAttack(self):
        await self.client.send_message(self.message.channel, "It's " + self.battler2.getName() + " 's turn.")
        await asyncio.sleep(2)
        await self.client.send_message()
        self.client.send_message

    async def initiatePvEBattle(self):
        #battler1 is player, battler2 is mob
        printBattleLog()
        determineWhoFirst(thePlayer, theMob)
        
        if isinstance(whoFirst, Player):
            mobAttack()
        
        await self.client.send_message(self.message.channel, "Available commands: !attack, !skill <id>, !items <id>, !run")
        returnCommand = client.wait_for_message(author=self.message.author)
        if returnCommand.content.startswith('!attack'):
            xxxx
