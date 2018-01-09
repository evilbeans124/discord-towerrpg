import os
import discord
import asyncio
import random
import math

from cogs.Mob import Mob

class BoarClass(Mob):
    mob_id = 1
    name = "Boar"
    current_hp = None
    max_hp = None
    current_mp = None
    max_mp = None
    level = None

    hp_regen = None #amount of hp regen per turn.
    mp_regen = None #amount of mp regen per turn.
    spell_power = None #magical only
    attack_power = None #physical only
    physical_defense = None
    magical_defense = None
    speed = None #faster speed = first chance in battle
    accuracy = None #affects both physical and magical
    parry_chance = None #100 = all physical attacks will be parryed, only with handheld wep
    critical_chance = None #100 = 100% crit, both mag and phy
    critical_damage_multiplier = None #both mag and phy
    block_chance = None #only works with shields, 100% = all blocked
    dodge_chance = None #100 = all dodged

    damage = None

    expGiven = None
    goldGiven = None
    
    def __init__(self, player):
        #super().__init__()
        self.createBoar(player)

    def getName(self):
        return self.name

    #the stats of the created boar is based on the character's level,
    #an internal luck generator and the current tower that the player is on
    #however, for now, to simplify things, it's all going to be the same.
    def createBoar(self, player):
        player_level = player.getLevel()
        self.level = random.randint(player_level - 3, player_level + 3)
        if self.level < 1:
            self.level = 1
        
        self.current_hp = 20 + self.level * 3
        self.max_hp = self.current_hp
        self.current_mp = 5
        self.max_mp = self.current_mp
        self.speed = random.randint(4, 6) + self.level * 0.05
        self.attack_power = random.randint(2, 3) + self.level * 0.75
        self.expGiven = random.randint(5, 10) * self.level
        self.goldGiven = random.randint(5, 10) * self.level

    def getCurrentHp(self):
        return self.current_hp

    def getMaxHp(self):
        return self.max_hp

    def getCurrentMp(self):
        return self.current_mp

    def getMaxMp(self):
        return self.max_mp

    def getSpeed(self):
        return self.speed

    def getAttack(self):
        return self.attack_power

    def getExp(self):
        return self.expGiven

    def getGold(self):
        return self.goldGiven

    def getLevel(self):
        return self.level

    def decrease_hp(self, hpToDecrease):
        self.current_hp -= hpToDecrease
