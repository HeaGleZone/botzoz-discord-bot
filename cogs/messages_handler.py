from discord.ext import commands

from musicbot_filters import *
from messages_filters import *


class MessagesHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('\n---------------------')
        print('     Bot running')
        print('---------------------\n')

    @commands.Cog.listener()
    async def on_message(self, message):
        # Don't check own messages
        if (self.bot.user == message.author):
            return

        await self.delete_messages(message)

    async def delete_messages(self, message):
        # Props
        content = message.content
        channel = message.channel
        author = message.author
        embeds = message.embeds
        attachments = message.attachments
        mentions = message.mentions

        # Delete music bot commands and message if not in the right channel
        if not(is_music_channel(channel)):
            if is_musicbot_command(content) or author.bot:
                print('Deleted message - music-bot restrictions')
                await message.delete()

        # Delete embeds in the wrong channel
        if not(are_embeds_allowed(channel)) and check_embeds(embeds):
            print('Deleted message - embeds restrictions')
            await message.delete()

        # Delete attachments in the wrong channel
        if not(are_attachments_allowed(channel)) and check_attachments(attachments):
            print('Deleted message - attachments restrictions')
            await message.delete()

        # Delete mentions in the wrong channel
        if not(are_mentions_allowed(channel)) and check_mentions(mentions):
            print('Deleted message - mentions restrictions')
            await message.delete()


def setup(bot):
    bot.add_cog(MessagesHandler(bot))
