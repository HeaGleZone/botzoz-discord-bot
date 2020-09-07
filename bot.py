"Discord Bot entry point"

from discord.ext import commands
from token_handler import get_token
from extensions_handler import load_extension

# Defining the Bot
print('---- Botzoz Discord bot ---- \n')
bot = commands.Bot(command_prefix='$')

# Environment
TOKEN = get_token(enable_log=True)

# Extensions
extensions = ['cogs.messages_handler',
              'cogs.commands_handler', 'cogs.auto_posts']
load_extension(bot, extensions)

# Running Bot
try:
    bot.run(TOKEN)
except Exception as e:  # pylint: disable=broad-except
    print('\n\nThe bot could\'t run:')
    print(e)
