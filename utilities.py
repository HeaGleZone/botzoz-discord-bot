"Bot's Utilities"


def get_voice_channels(bot, user_guild):
    'Returns a list of the server voice channels'

    for guild in bot.guilds:
        if user_guild == guild.id:
            return guild.voice_channels

    return []


def get_voice_users(bot, user_guild):
    'Returns a list of the server users connected to a voice channel'

    voice_members = []
    for voice_channel in get_voice_channels(bot, user_guild):
        for member in voice_channel.members:
            voice_members.append(member)
    return voice_members
