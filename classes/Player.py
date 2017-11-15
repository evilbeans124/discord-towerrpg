import os
import discord
import asyncio

from classes.Classes import Classes

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
    player_class = None #representation of the player's class. Not stored on the player's file. Will fix this later, right now i have no idea how lol
    message_author_id = None #client's id
    current_tower_level = None #The level of the current tower its on

    def __init__(self, newUser, c, message_author_id):
        if newUser:
            self.current_hp = 50
            self.max_hp = 50
            self.gold = 100
            self.experience = 0
            self.experienceToLevel = 1000
            self.level = 1

            self.strength = 5
            self.dexterity = 5
            self.intellect = 5

            self.hp_regen = 0
            self.mp_regen = 0
            self.spell_power = 0
            self.attack_power = 0
            self.physical_defense = 0
            self.magical_defense = 0
            self.speed = 5
            self.accuracy = 0
            self.parry_chance = 0
            self.critical_chance = 0
            self.critical_damage_multiplier = 0
            self.block_chance = 0
            self.dodge_chance = 0
            
            self.player_class = Classes(0)
            self.class_id = 0
            self.message_author_id = message_author_id
            self.current_tower_level = 1
            
            self.updateFile(self.message_author_id)
        else:
            self.current_hp = c[0]
            self.max_hp = c[1]
            self.gold = c[2]
            self.experience = c[3]
            self.experienceToLevel = c[4]
            self.level = c[5]

            self.strength = c[6]
            self.dexterity = c[7]
            self.intellect = c[8]

            self.hp_regen = c[9]
            self.mp_regen = c[10]
            self.spell_power = c[11]
            self.attack_power = c[12]
            self.physical_defense = c[13]
            self.magical_defense = c[14]
            self.speed = c[15]
            self.accuracy = c[16]
            self.parry_chance = c[17]
            self.critical_chance = c[18]
            self.critical_damage_multiplier = c[19]
            self.block_chance = c[20]
            self.dodge_chance = c[21]

            self.player_class = Classes(c[22])
            self.class_id = c[22]
            self.message_author_id = c[23]
            self.current_tower_level = c[24]

    def getLevel(self):
        return self.level

    def getTowerLevel(self):
        return self.current_tower_level

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

    def increase_level(self):
        level += 1
        self.experience -= experienceToLevel

        self.updateFile(self.message_author_id)

    def decrease_hp(self, hpToDecrease):
        self.current_hp -= hpToDecrease

        self.updateFile(self.message_author_id)

    def decrease_exp(self, expToDecrease):
        self.experience -= expToDecrease

        self.updateFile(self.message_author_id)

    def increase_experience(self, experienceGained):
        self.experience += experienceGained
        while (self.experience >= experienceToLevel):
            self.increase_level()
            self.newExperienceToLevel()

        self.updateFile(self.message_author_id)

    def newExperienceToLevel(self):
        self.experienceToLevel *= 2

        self.updateFile(self.message_author_id)

    def setClass(self, theClassId):
        self.class_id = theClassId
        self.player_class = Classes(theClassId)
        
        self.updateFile(self.message_author_id)
        
    def getClassId(self):
        return self.class_id

    def getClass(self):
        return self.player_class

    def updateFile(self, message_author_id):
        filepath = os.path.join('/Users/orion01px2018/Desktop/discord-towerrpg/player_files/', str(message_author_id) + '.txt')
        
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
        f.write(str(self.message_author_id))
        f.write("\r\n")
        f.write(str(self.current_tower_level))
        f.write("\r\n")
        f.close()
