import os
import discord
import asyncio

from classes.Mob import Mob
import random

class NumbersHandler:
    @classmethod
    def whichMobToEncounter(self): #depends on SO MANY THINGS
        #for now this will be simplified to equal chance for every mob
        #in allMobs array
        allMobs = Mob.getAllMobs()
        randomNum = random.randint(0, len(allMobs) - 1)
        return allMobs[randomNum]
