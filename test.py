import discord
from discord.ext import commands

import sys, traceback

def determinePrefix(bot, message):
    """Determine any kind of Prefix"""

    prefixes = ['!?', '!']

    #this only gets called if the message is not passed in the server.
    #remember, guild means server
    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)

description = 'RPG!'
initial_extensions = ['cogs.start']

bot = commands.Bot(command_prefix=determinePrefix, description=description)

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    #await bot.change_presence(game=discord.Game(name='Cogs Example', type=1, url='https://twitch.tv/kraken'))
    await bot.change_presence(game=discord.Game(name='Developping...', type=0))

    # Here we load our extensions(cogs) listed above in [initial_extensions].
    if __name__ == '__main__':#if the program is being run by itself, else it is being imported from another module
        for extension in initial_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()
    print(f'Successfully logged in and booted...!')

@bot.check
async def globalCheck(ctx):
    start_cog = bot.get_cog('Start')
    isPlayer = await start_cog.getIsPlayer(ctx)
    cmd = ctx.command.name

    #ensuring player to be an actual player object
    if not isPlayer:
        if cmd == 'login' or cmd == 'register':
            return True
        else:
            await ctx.send(f'{ctx.author.name}, you need to !login first!')
            return False

    player = await start_cog.getPlayer(ctx)
    print(player)

    #checking whether player has chosen class or not
    hasChosenClass = not await start_cog.hasNotChosenClass(ctx)
    if not hasChosenClass:
        if cmd == 'login' or cmd == 'register' or cmd == 'classchoose' or cmd == 'classes':
            return True
        else:
            await ctx.send(f'{ctx.author.name}, you need to choose a class first. Please choose one by using the command !classchoose <id>. To read more about each class, do !classes.')
            return False
    else:
        if cmd == 'classchoose':
            await ctx.send(f'{ctx.author.name}, you have already chosen a class! Your current class is {player.getClass().getClassName()}.')
            return False
    return True

bot.run('Mzc4MjI4MDQ3MzcyODc3ODI0.DOYh9A.pGe81FZzMqqMCgsLbNm_ijZ2E1s', bot=True, reconnect=True)
