import discord
import asyncio
import os

from classes.Player import Player

#more of an event handler class than anything

player = None
logged_in = False

client = discord.Client()

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

@client.event
async def newPlayerEvent():
    await client.send_message(message.channel, "Welcome to TowerRPG, a text-based RTS MMORPG on Discord!")
    await asyncio.sleep(2)
    await client.send_message(message.channel, "Please choose your class using the command !classchoose <id>. To read more about each class, do !classes")

@client.event
async def readLore():
    await client.send_message(message.channel, "INSERT LORE HERE")
    await asyncio.sleep(2)
    await client.send_message(message.channel, "INSERT LORE HERE")

@client.event
async def checkRegister(message):
    filepath = os.path.join('/Users/orion01px2018/Desktop/disc/player_files/', client.user.id + '.txt')
    if not os.path.exists('/Users/orion01px2018/Desktop/disc/player_files'):
        os.makedirs('/Users/orion01px2018/Desktop/disc/player_files')

        await client.send_message(message.channel, "You have sucessfully registered.")
        await newPlayerEvent()

        player = Player(true, None, client.user.id)
    else:
        await client.send_message(message.channel, "You have already registered before, please do !login instead.")

@client.event
async def checkLogin(message):
    filepath = os.path.join('/Users/orion01px2018/Desktop/disc/player_files/', client.user.id + '.txt')
    if os.path.exists('/Users/orion01px2018/Desktop/disc/player_files'):
        c = read_integers(filepath)
        player = Player(false, c, client.user.id)

        logged_in = True
        await client.send_message(message.channel, "You have successfully logged in. Welcome back!")
    else:
        await client.send_message(message.channel, "You haven't registed yet, please do !register.")

@client.event
async def on_ready():
    print('Logged in')

@client.event
async def classChooseEvent():
    if logged_in:
        return None
    else:
        await.client.send_message(message.channel, "You are not logged in.")

@client.event
async def classInfoEvent():
    if logged_in:
        return None
    else:
        await.client.send_message(message.channel, "You are not logged in.")

@client.event
async def getStatsEvent():
    if logged_in:
        return None
    else:
        await.client.send_message(message.channel, "You are not logged in.")

@client.event
async def lookForBattle():
    if logged_in:
        return None
    else:
        await.client.send_message(message.channel, "You are not logged in.")
    
@client.event
async def on_message(message):
    if message.content.startswith('!register'):
        await checkRegister(message)
        
    elif message.content.startswith('!login'):
        if logged_in:
            await client.send_message(message.channel, "You are already logged in.")
        else:
            await checkLogin(message)
    elif message.content.startswith('!classchoose'):
        await classChooseEvent()
    elif message.content.startswith('!classes'):
        await classInfoEvent()
    elif message.content.startswith('!stats'):
        await getStatsEvent()
    elif message.content.startswith('!battle'):
        await lookForBattle()



























        
    
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'Done sleeping')

    if message.content.startswith('$cool'):
        await client.send_message(message.channel, 'Who is cool? Type $name namehere')

        def check(msg):
            return msg.content.startswith('$name')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('$name'):].strip()
        await client.send_message(message.channel, '{} is cool indeed'.format(name))
        
client.run('Mzc4MjI4MDQ3MzcyODc3ODI0.DOYh9A.pGe81FZzMqqMCgsLbNm_ijZ2E1s')
