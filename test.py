import discord
import asyncio
import os

from classes.Player import Player
from classes.Mob import Mob
from classes.NumbersHandler import NumbersHandler
from classes.Battle import Battle

#more of an event handler class than anything

player = None
logged_in = False
in_battle = False

client = discord.Client()

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

@client.event
async def newPlayerEvent(message):
    #await readLore(message)
    await client.send_message(message.channel, "Welcome to TowerRPG, " + message.author.name + ". TowerRPG is a text-based RTS MMORPG on Discord!")
    await asyncio.sleep(2)
    await client.send_message(message.channel, message.author.name + ", please choose your class using the command !classchoose <id>. To read more about each class, do !classes")

@client.event
async def readLore(message):
    await client.send_message(message.channel, "INSERT LORE HERE")
    await asyncio.sleep(2)
    await client.send_message(message.channel, "INSERT LORE HERE")

@client.event
async def checkRegister(message):
    global logged_in
    global player
    if logged_in == True:
        await client.send_message(message.channel, message.author.name + ", you are already logged in.")
    else:    
        if os.path.isfile('/Users/orion01px2018/Desktop/discord-towerrpg/player_files/' + str(message.author.id) + '.txt'):
            await client.send_message(message.channel, message.author.name + ", you have already registered before, please do !login instead.")
        else:
            f = open('/Users/orion01px2018/Desktop/discord-towerrpg/player_files/' + str(message.author.id) + '.txt', "w+")
            f.close()

            logged_in = True

            await client.send_message(message.channel, message.author.name + ", you have sucessfully registered.")
            await newPlayerEvent(message)

            player = Player(True, None, message.author.id)

@client.event
async def checkLogin(message):
    global logged_in
    global player
    if logged_in:
        await client.send_message(message.channel, message.author.name + ", you are already logged in.")
    else:
        filepath = '/Users/orion01px2018/Desktop/discord-towerrpg/player_files/' + message.author.id + '.txt'
        if os.path.isfile(filepath):
            c = read_integers(filepath)
            player = Player(False, c, message.author.id)

            logged_in = True
            await client.send_message(message.channel, message.author.name + ", you have successfully logged in. Welcome back!")
        else:
            await client.send_message(message.channel, message.author.name + ", you haven't registed yet, please do !register.")

@client.event
async def on_ready():
    print('Logged in')

@client.event
async def classChooseEvent(message):
    if logged_in:
        global player
        if player.getClassId() == 0:
            class_id = int(message.content.split()[-1])
            if (class_id < (len(player.getClass().getAllClasses()))) and (not class_id == 0):
                player.setClass(class_id)
                await client.send_message(message.channel, message.author.name + ", you have successfully chose " + player.getClass().getClassName() + " as your class!") #specify which class later
            else:
                await client.send_message(message.channel, "Invalid class id, " + message.author.name + ". Please try again.")
        else:
            await client.send_message(message.channel, message.author.name + ", you have already chosen a class! Your current class is " + player.getClass().getClassName())
    else:
        await client.send_message(message.channel, message.author.name + ", you are not logged in.")

@client.event
async def classInfoEvent(message):
    if logged_in:
        return None
    else:
        await client.send_message(message.channel, message.author.name + ", you are not logged in.")

@client.event
async def getStatsEvent(message):
    if logged_in:
        await client.send_message(message.channel, message.author.name + "Hp: " + str(player.getCurrentHp()))
    else:
        await client.send_message(message.channel, message.author.name + ", you are not logged in.")

@client.event
async def lookForBattle(message):
    global player
    global client
    global in_battle
    if logged_in:
        if in_battle:
            await client.send_message(message.channel, message.author.name + ", you are currently in a battle!")
        else:
            waiting_message = await client.send_message(message.channel, message.author.name + ", you are currently searching for a battle....")
            await NumbersHandler.encounterWait()

            #add animation code for the .'s to increase here
        
            theMob = Mob(NumbersHandler.whichMobToEncounter(), player)
            mobToEncounter = theMob.getCurrentMob()
            await client.send_message(message.channel, message.author.name + ", you have encountered a " + mobToEncounter.getName() + ". Battle begins!")
            in_battle = True
            thebattle = Battle(player, mobToEncounter, message, client)
            in_battle = False
    else:
        await client.send_message(message.channel, message.author.name + ", you are not logged in.")
    
@client.event
async def on_message(message):
    if message.content.startswith('!register'):
        await checkRegister(message)
    elif message.content.startswith('!login'):
        await checkLogin(message)
    elif message.content.startswith('!classchoose'):
        await classChooseEvent(message)
    elif message.content.startswith('!classes'):
        await classInfoEvent(message)
    elif message.content.startswith('!stats'):
        await getStatsEvent(message)
    elif message.content.startswith('!battle'):
        await lookForBattle(message)


























        
    
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    if message.content.startswith('$cool'):
        await client.send_message(message.channel, 'Who is cool? Type $name namehere')

        def check(msg):
            return msg.content.startswith('$name')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('$name'):].strip()
        await client.send_message(message.channel, '{} is cool indeed'.format(name))
    
client.run('Mzc4MjI4MDQ3MzcyODc3ODI0.DOYh9A.pGe81FZzMqqMCgsLbNm_ijZ2E1s')
