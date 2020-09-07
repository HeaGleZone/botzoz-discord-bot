"Loads extensions from the extensions list into the bot"

import sys


def load_extension(bot, extensions):
    "Loads extensions from the extensions list into the bot"

    print('Extensions:')
    if len(extensions) == 0:
        print(' !- No extensions loaded in!')
        return

    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:  # pylint: disable=broad-except
            print(f' !- Failed to load extension {extension}!')
            print(e)
            sys.exit()
        else:
            print(f' - "{extension}" loaded in.')
