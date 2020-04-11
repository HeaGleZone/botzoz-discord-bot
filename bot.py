from discord.ext import commands
from token_handler import get_token
from extensions_handler import load_extension

# Defining the Bot
print('---- Botzoz Discord bot ---- \n')
bot = commands.Bot(command_prefix='$')

# Environment
TOKEN = get_token(enableLog=True)

# Extensions
extensions = ['cogs.messages_handler',
              'cogs.commands_handler', 'cogs.auto_posts']
load_extension(bot, extensions)

# Running Bot
try:
    bot.run(TOKEN)
except Exception as e:
    print('\n\nThe bot could\'t run:')
    print(e)
