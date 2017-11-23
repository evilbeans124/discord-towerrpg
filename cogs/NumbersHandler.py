import os
import discord
import asyncio

from classes.Mob import Mob
from classes.Skills import Skills
import random

class NumbersHandler:

    #actually none of these should be a class method
    #ill fix it later lol

    randomTime = None
    
    @classmethod
    def whichMobToEncounter(cls): #depends on SO MANY THINGS
        #for now this will be simplified to equal chance for every mob
        #in allMobs array
        allMobs = Mob.getAllMobs()
        randomNum = random.randint(0, len(allMobs) - 1)
        return allMobs[randomNum]

    @classmethod
    async def encounterWait(cls):
        cls.randomTime = random.random() * 10
        await asyncio.sleep(cls.randomTime)

    @classmethod
    def getRandomTime(cls):
        return cls.randomTime
