import discord
import asyncio
import os
import random
import math

from classes.Player import Player
from classes.Mob import Mob
from classes.BoarClass import BoarClass
from classes.NumbersHandler import NumbersHandler

class Battle:
    whosTurn = None
    battler1 = None
    battler2 = None
    damageDealtBy1 = None
    damageDealtBy2 = None
    message = None
    client = None
    currentRound = None

    #Boarclass is supposed to be Mob
    def __init__(self, battler1, battler2, message, client):
        self.battler1 = battler1
        self.battler2 = battler2
        self.message = message
        self.client = client
        self.damageDealtBy1 = 0 #these needs to be arrays
        self.damageDealtBy2 = 0
        self.currentRound = 1
        if isinstance(battler1, Player) and isinstance(battler2, BoarClass):
            asyncio.ensure_future(self.initiatePvEBattle())

    async def printBattleLog(self):
        await self.client.send_message(self.message.channel, "```========== " + self.message.author.name + " VS " + self.battler2.getName()
                                       + " ==========\n\n" + self.message.author.name + "'s HP: " + str(self.battler1.getCurrentHp())
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
        returnCommand = await self.client.wait_for_message(author=self.message.author)
        if returnCommand.content.startswith('!attack'):
            await self.playerAttack()
        else:
            await self.client.send_message(self.message.channel, "Invalid command. Please try again.")

    async def playerAttack(self):
        self.damageDealtBy1 = math.floor(self.battler1.getAttack() * 1.5)
        await self.client.send_message(self.message.channel, self.message.author.name + " uses normal attack. Dealt " + str(self.damageDealtBy1) + " damage.")
        self.battler2.decrease_hp(self.damageDealtBy1)

        self.whosTurn = self.battler2

    async def playerSkill(self):
        return None

    async def playerItem(self):
        return None

    async def playerRun(self):
        return None

    async def mobAttack(self):
        await self.client.send_message(self.message.channel, "It's " + self.battler2.getName() + "'s turn.")
        await asyncio.sleep(1)

        action = await self.mobGetAction()

        await self.client.send_message(self.message.channel, action)
        self.battler1.decrease_hp(self.damageDealtBy2)

        self.whosTurn = self.battler1

    async def mobGetAction(self):
        if random.randint(1, 4) == -1: #execute a skill
            #skill = xxx
            #getSkillName = random.randint(0, len(Skills.getAllSkills))
            #getSkillDamage = 
            
            #return self.name " uses " + getSkillName + ". Dealt "
            return None
        else: #execute a regular attack
            self.damageDealtBy2 = math.floor(self.battler2.getAttack() * 1.5)
            return self.battler2.getName() + " uses normal attack. Dealt " + str(self.damageDealtBy2) + " damage."

    async def initiatePvEBattle(self):
        #battler1 is player, battler2 is mob
        self.determineWhoFirst()

        while self.battler1.getCurrentHp() > 0 and self.battler2.getCurrentHp() > 0:
            await self.printBattleLog()
            if isinstance(self.whosTurn, Player):
                await self.playerAction()
            else:
                await self.mobAttack()

        if self.battler1.getCurrentHp() <= 0:
            await self.client.send_message(self.message.channel, self.message.author.name + ". you have died!")#add punishment for lost
            await asyncio.sleep(1)
            await self.client.send_message(self.message.channel, self.message.author.name +
                                           ", as punishment for your death, you lose 20% of your exp and gold.")
            self.battler1.decrease_gold(self.battler1.getGold() / 5)
            self.battler1.decrease_exp(self.battler1.getExp() / 5)
            self.battler1.setHp(self.battler1.getMaxHp())
            
        elif self.battler2.getCurrentHp() <= 0:
            await self.client.send_message(self.message.channel, "Congratulations! " + self.message.author.name + " has won the battle!")
            await asyncio.sleep(1)
            await self.client.send_message(self.message.channel, self.message.author.name +
                                           ", you obtained " + str(self.battler2.getExp()) + " exp and " + str(self.battler2.getGold()) + " gold.")

            self.battler1.increase_exp(self.battler2.getExp())
            self.battler1.increase_gold(self.battler2.getGold())

            await asyncio.sleep(1)
            
