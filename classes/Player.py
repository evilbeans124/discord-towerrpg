import os
import discord
import asyncio

from class.Classes import Classes

class Player:
    current_hp = None
    max_hp = None
    current_mp = None
    max_mp = None
    gold = None
    experience = None
    experienceToLevel = None
    level = None

    strength = None #increases attack_power, hp, physical defense, hp regen
    dexterity = None #increases speed, accuracy, dodge chance, crit multi/chance
    intellect = None #increases spell power, magic defense, mp, mp regen

    hp_regen = None #amount of hp regen per turn. not in combat = per second
    mp_regen = None #amount of mp regen per turn. not in combat = per second
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
    
    class_id = None #1 = Warrior 2 = Ranger 3 = Mage
    client_user_id = None #client's id

    def __init__(newUser, c, client.user.id):
        if newUser:
            current_hp = 50
            max_hp = 50
            gold = 100
            experience = 0
            experienceToLevel = 1000
            level = 1

            strength = 5
            dexterity = 5
            intellect = 5

            hp_regen = 0
            mp_regen = 0
            spell_power = 0
            attack_power = 0
            physical_defense = 0
            magical_defense = 0
            speed = 1
            accuracy = 0
            parry_chance = 0
            critical_chance = 0
            critical_damage_multiplier = 0
            block_chance = 0
            dodge_chance = 0
            
            class_id = 0 #NOT SURE YET LOL
            client_user_id = client.user.id #probably not the best way to go but i'll fix it.
            
            updateFile(client_user_id)
        else:
            current_hp = c[0]
            max_hp = c[1]
            gold = c[2]
            experience = c[3]
            experienceToLevel = c[4]
            level = c[5]

            strength = c[6]
            dexterity = c[7]
            intellect = c[8]

            hp_regen = c[9]
            mp_regen = c[10]
            spell_power = c[11]
            attack_power = c[12]
            physical_defense = c[13]
            magical_defense = c[14]
            speed = c[15]
            accuracy = c[16]
            parry_chance = c[17]
            critical_chance = c[18]
            critical_damage_multiplier = c[19]
            block_chance = c[20]
            dodge_chance = c[21]

            class_id = c[22]
            client_user_id = c[23]

    def increase_level(self):
        level++
        self.experience -= experienceToLevel

    def decrease_hp(self, hpToDecrease):
        self.current_hp -= hpToDecrease

    def decrease_exp(self, expToDecrease):
        self.experience -= expToDecrease

    def increase_experience(self, experienceGained):
        self.experience += experienceGained
        while (self.experience >= experienceToLevel):
            increase_level()
            newExperienceToLevel()

    def newExperienceToLevel(self):
        experienceToLevel *= 2

    def setClass(self, classs): #tbh i have no idea if this will actually work
        self.class_id = classs.getId()

    def updateFile(self, client.user.id):
        filepath = os.path.join('/Users/orion01px2018/Desktop/disc/player_files', client.user.id + '.txt')
        
        f = open(filepath, "w+")
        f.write(str(self.current_hp))
        f.write("\r\n")
        f.write(str(self.max_hp))
        f.write("\r\n")
        f.write(str(self.gold))
        f.write("\r\n")
        f.write(str(self.experience))
        f.write("\r\n")
        f.write(str(self.experienceToLevel))
        f.write("\r\n")
        f.write(str(self.level))
        f.write("\r\n")
        f.write(str(self.strength))
        f.write("\r\n")
        f.write(str(self.dexterity))
        f.write("\r\n")
        f.write(str(self.intellect))
        f.write("\r\n")
        f.write(str(self.hp_regen))
        f.write("\r\n")
        f.write(str(self.mp_regen))
        f.write("\r\n")
        f.write(str(self.spell_power))
        f.write("\r\n")
        f.write(str(self.attack_power))
        f.write("\r\n")
        f.write(str(self.physical_defense))
        f.write("\r\n")
        f.write(str(self.magical_defense))
        f.write("\r\n")
        f.write(str(self.speed))
        f.write("\r\n")
        f.write(str(self.accuracy))
        f.write("\r\n")
        f.write(str(self.parry_chance))
        f.write("\r\n")
        f.write(str(self.critical_chance))
        f.write("\r\n")
        f.write(str(self.critical_damage_multiplier))
        f.write("\r\n")
        f.write(str(self.block_chance))
        f.write("\r\n")
        f.write(str(self.dodge_chance))
        f.write("\r\n")
        f.write(str(self.class_id))
        f.write("\r\n")
        f.write(str(self.client_user_id))
        f.write("\r\n")
        f.close()
