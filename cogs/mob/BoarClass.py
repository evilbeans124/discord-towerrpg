import os
import discord
import asyncio
import random
import math

class BoarClass:
    mob_id = 1
    name = "Boar"
    current_hp = None
    max_hp = None
    current_mp = None
    max_mp = None
    level = None

    strength = None #increases attack_power, hp, physical defense, hp regen
    dexterity = None #increases speed, accuracy, dodge chance, crit multi/chance
    intellect = None #increases spell power, magic defense, mp, mp regen

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
    dodge_chance = None #100% = all dodged

    damage = None

    expGiven = None
    goldGiven = None
    
    def __init__(self, player):
        self.createBoar(player)

    def getName(self):
        return self.name

    #the stats of the created boar is based on the character's level,
    #an internal luck generator and the current tower that the player is on
    #however, for now, to simplify things, it's all going to be the same.
    def createBoar(self, player):
        self.current_hp = 20
        self.max_hp = 20
        self.current_mp = 5
        self.max_mp = 5
        self.speed = random.randint(4, 6)
        self.attack_power = random.randint(2, 3)
        self.expGiven = random.randint(5, 10)
        self.goldGiven = random.randint(5, 10)

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

    def decrease_hp(self, hpToDecrease):
        self.current_hp -= hpToDecrease
