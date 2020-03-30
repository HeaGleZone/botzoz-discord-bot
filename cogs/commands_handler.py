import discord
from discord.ext import commands
import random
from utilities import get_voice_channels, get_voice_users


class CommandsHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shuffle(self, ctx):
        'Shuffles voice users between voice channels'

        author = ctx.message.author
        isAdmin = author.guild_permissions.administrator
        user_guild = author.guild.id
        voice_channels = get_voice_channels(self.bot, user_guild)
        voice_users = get_voice_users(self.bot, user_guild)

        if (isAdmin):
            print(f'User {author} is shuffling voice members.')
            await ctx.send('Shuffling voice users.')
            for user in voice_users:
                rnd_channel = random.choice(voice_channels)
                await user.move_to(rnd_channel)
        else:
            print(f'User {author} has no permissions to shuffle voice users.')
            await ctx.send('You don\'t have permissions to do that.')


def setup(bot):
    bot.add_cog(CommandsHandler(bot))
