import discord
import asyncio
import random
import math

class PvEBattle:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob
        self.roundnumber = 1
        self.currentTurn = self.determineWhoFirst()

    def getPlayer(self):
        return self.player

    def getMob(self):
        return self.mob

    def getCurrentTurn(self):
        return self.currentTurn

    def getRoundNumber(self):
        return self.roundnumber

    def increaseRoundNumber(self):
        self.roundnumber += 1

    def determineWhoFirst(self):
        if self.player.getSpeed() > self.mob.getSpeed():
            return self.player
        elif self.player.getSpeed() < self.mob.getSpeed():
            return self.mob
        else:
            if random.randint(1, 2) == 1:
                return self.player
            else:
                return self.mob

    def changeTurns(self):
        if self.currentTurn == self.player:
            self.currentTurn = self.mob
        elif self.currentTurn == self.mob:
            self.currentTurn = self.player
            
    def playerAttack(self):
        dmg = math.floor(self.player.getAttack() * 1.5)
        self.mob.decrease_hp(dmg)
        
        return dmg

    def playerSkill(self):
        string = 'skill'

    def mobAction(self):
        if random.randint(1, 4) == -1:
            #skill = xxx
            #getSkillName = random.randint(0, len(Skills.getAllSkills))
            #getSkillDamage = 
            
            #return self.name " uses " + getSkillName + ". Dealt "
            return 'skill'
            #
        else: #execute a regular attack
            return 'attack'

    def mobAttack(self):
        dmg = math.floor(self.mob.getAttack() * 1.5)
        self.player.decrease_hp(dmg)
        
        return dmg
        
    def mobSkill(self):
        string = 'skill'
