import discord
from discord.ext import commands
import random
from utilities import get_voice_channels, get_voice_users


class CommandsHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def shuffle(self, ctx):
        'Shuffles voice users between voice channels'

        # Props
        author = ctx.message.author
        user_guild = author.guild.id
        voice_channels = get_voice_channels(self.bot, user_guild)
        voice_users = get_voice_users(self.bot, user_guild)

        # Response
        print(f'User {author} is shuffling voice members.')
        await ctx.send('Shuffling voice users.')
        for user in voice_users:
            rnd_channel = random.choice(voice_channels)
            await user.move_to(rnd_channel)

    @shuffle.error
    async def general_guild_only_error(self, ctx, error):
        # Props
        author = ctx.message.author

        # No DMs
        if isinstance(error, commands.NoPrivateMessage):
            print(f'User {author} has no permissions to shuffle voice users.')
            await ctx.send('Nope')
            return

        # Check permission
        if isinstance(error, commands.MissingPermissions):
            print(
                f'User {author} has no permissions to run {ctx.message.content}.')
            await ctx.send('You\'re not allowed to do that. Nice try.')


def setup(bot):
    bot.add_cog(CommandsHandler(bot))
