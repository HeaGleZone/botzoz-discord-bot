def load_extension(bot, extensions):
    'Loads extensions from the extensions list into the bot'

    print('Extensions:')
    if len(extensions) == 0:
        print(' !- No extensions loaded in!')
        return

    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f' !- Failed to load extension {extension}!')
            print(e)
            exit()
        else:
            print(f' - "{extension}" loaded in.')
