import os
import discord
import asyncio
import random

class Mob:

    #a subclass of this class would be the actual mob itself
    #eg zombie, boar

    #the subclass only gets created upon encounter of a battle
    #after the battle its gone forever lul

    #this class is only called by the subclass

    current_mob = None
    
    #name = None
    #current_hp = None
    #max_hp = None
    #current_mp = None
    #max_mp = None
    #level = None

    #strength = None #increases attack_power, hp, physical defense, hp regen
    #dexterity = None #increases speed, accuracy, dodge chance, crit multi/chance
    #intellect = None #increases spell power, magic defense, mp, mp regen

    #hp_regen = None #amount of hp regen per turn.
    #mp_regen = None #amount of mp regen per turn.
    #spell_power = None #magical only
    #attack_power = None #physical only
    #physical_defense = None
    #magical_defense = None 
    #speed = None #faster speed = first chance in battle
    #accuracy = None #affects both physical and magical
    #parry_chance = None #100 = all physical attacks will be parryed, only with handheld wep
    #critical_chance = None #100 = 100% crit, both mag and phy
    #critical_damage_multiplier = None #both mag and phy
    #block_chance = None #only works with shields, 100% = all blocked
    #dodge_chance = None #100% = all dodged

    @classmethod
    def encounterRandomMob(cls, player):
        allMobs = Mob.__subclasses__() #this is an array
        randomClassNum = random.randint(0, len(allMobs) - 1)
        return allMobs[randomClassNum](player)

    @classmethod
    def getAllMobs(cls):
        return cls.__subclasses__()

    def __init__(self):
        hi = "hi"

    def getCurrentMob(self):
        return self.current_mob
