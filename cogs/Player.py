import os
import discord
import asyncio

import json
import io

from cogs.Classes import Classes

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
    
    class_id = None #0 = Hasn't chose 1 = Warrior 2 = Ranger 3 = Mage
    player_class = None #representation of the player's class. Not stored on the player's file. Will fix this later, right now i have no idea how lol
    message_author_id = None #client's id
    current_tower_level = None #The level of the current tower the client is on

    x_position = None
    y_position = None

    def __init__(self, message_author_id):
        with open(f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{str(message_author_id)}.json') as data_file:
            data = json.load(data_file)

            #statistics
            self.current_hp = data['statistics']['current_hp']
            self.max_hp = data['statistics']['max_hp']
            self.current_mp = data['statistics']['current_mp']
            self.max_mp = data['statistics']['max_mp']
            self.gold = data['statistics']['gold']
            self.experience = data['statistics']['experience']
            self.experienceToLevel = data['statistics']['experienceToLevel']
            self.level = data['statistics']['level']
            self.current_tower_level = data['statistics']['current_tower_level']

            #attributes
            self.strength = data['attributes']['strength']
            self.dexterity = data['attributes']['dexterity']
            self.intellect = data['attributes']['intellect']
            self.hp_regen = data['attributes']['hp_regen']
            self.mp_regen = data['attributes']['mp_regen']
            self.spell_power = data['attributes']['spell_power']
            self.attack_power = data['attributes']['attack_power']
            self.physical_defense = data['attributes']['physical_defense']
            self.magical_defense = data['attributes']['magical_defense']
            self.speed = data['attributes']['speed']
            self.accuracy = data['attributes']['accuracy']
            self.parry_chance = data['attributes']['accuracy']
            self.critical_chance = data['attributes']['critical_chance']
            self.critical_damage_multiplier = data['attributes']['critical_damage_multiplier']
            self.block_chance = data['attributes']['block_chance']
            self.dodge_chance = data['attributes']['dodge_chance']

            #personal_no_display
            self.class_id = data['personal_no_display']['class_id']
            self.message_author_id = data['personal_no_display']['message_author_id']
            self.x_position = data['personal_no_display']['coordinates'][0]
            self.y_position = data['personal_no_display']['coordinates'][1]

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

    def getAttack(self):
        return self.attack_power

    def getSpeed(self):
        return self.speed

    def getExp(self):
        return self.experience

    def getExpToLevel(self):
        return self.experienceToLevel

    def getGold(self):
        return self.gold

    def getClassId(self):
        return self.class_id

    def getXPos(self):
        return self.x_position

    def getYPos(self):
        return self.y_position

    def setHp(self, hpToSet):
        self.current_hp = hpToSet

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

    def decrease_gold(self, goldToDecrease):
        self.gold -= goldToDecrease

        self.updateFile(self.message_author_id)

    def increase_gold(self, goldToIncrease):
        self.gold += goldToIncrease

        self.updateFile(self.message_author_id)

    def increase_exp(self, experienceGained):
        self.experience += experienceGained
        while (self.experience >= self.experienceToLevel):
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
        filepath = f'/Users/orion01px2018/Desktop/discord-towerrpg/player_files/{str(message_author_id)}'
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str

        data = {'attributes': {'strength': self.strength,
                               'dexterity': self.dexterity,
                               'intellect': f'{str(self.intellect)}',
                               'hp_regen': f'{str(self.hp_regen)}',
                               'mp_regen': f'{str(self.mp_regen)}',
                               'spell_power': f'{str(self.spell_power)}',
                               'attack_power': f'{str(self.attack_power)}',
                               'physical_defense': f'{str(self.physical_defense)}',
                               'magical_defense': f'{str(self.magical_defense)}',
                               'speed': f'{str(self.speed)}',
                               'accuracy': f'{str(self.accuracy)}',
                               'parry_chance': f'{str(self.parry_chance)}',
                               'critical_chance': f'{str(self.critical_chance)}',
                               'critical_damage_multiplier': f'{str(self.critical_damage_multiplier)}',
                               'block_chance': f'{str(self.block_chance)}',
                               'dodge_chance': f'{str(self.dodge_chance)}'},
                'statistics': {'current_hp': f'{str(self.current_hp)}',
                               'max_hp': f'{str(self.max_hp)}',
                               'current_mp': f'{str(self.current_mp)}',
                               'max_mp': f'{str(self.max_mp)}',
                               'level': f'{str(self.level)}',
                               'experience': f'{str(self.experience)}',
                               'experienceToLevel': f'{str(self.experienceToLevel)}',
                               'gold': f'{str(self.gold)}',
                               'current_tower_level': f'{str(self.current_tower_level)}'},
                'personal_no_display': {'class_id': f'{str(self.class_id)}',
                               'message_author_id': f'{str(self.message_author_id)}',
                               'coordinates': [self.x_position, self.y_position]}}

        with io.open(f'{filepath}.json', 'w+', encoding='utf8') as outfile:
            str_ = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))
    
