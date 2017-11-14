import discord
import asyncio
import os

from classes.Player import Player
from classes.Mob import Mob
from classes.BoarClass import BoarClass

class Battle:
    battler1 = None
    battler2 = None
    message = None
    client = None

    #Boarclass is supposed to be Mob
    def __init__(self, battler1, battler2, message, client):
        self.battler1 = battler1
        self.battler2 = battler2
        self.message = message
        self.client = client
        if isinstance(battler1, Player) and isinstance(battler2, BoarClass):
            asyncio.ensure_future(self.initiatePvEBattle(battler1, battler2))

    async def initiatePvEBattle(self, thePlayer, theMob):
        await self.client.send_message(self.message.channel, "REACHED")
    
