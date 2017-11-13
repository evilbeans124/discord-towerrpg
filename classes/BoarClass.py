import os
import discord
import asyncio

class BoarClass(Classes):
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
    
    def __init__(self, player):
        self.createBoar(player)

    #the stats of the created boar is based on the character's level, an internal luck generator, the current tower that the player is on
    #and 
    def createBoar(self):
        self.

    
