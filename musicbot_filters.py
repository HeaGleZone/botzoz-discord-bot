'Music Bot helper functions'


def is_music_channel(channel):
    'Checks if the channel music channel.'

    channel = str(channel)
    return channel == 'music-bot'


def is_musicbot_command(content):
    'Checks if the message starts with a music-bot symbol.'

    return content.startswith('-') or content.startswith('!')
