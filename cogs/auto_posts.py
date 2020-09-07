"Automatic Posts - with timers"

import asyncio
import discord
from discord.ext import commands
import aiohttp


class AutoPosts(commands.Cog):
    "Automatic Posts - with timers"

    def __init__(self, bot):
        self.bot = bot
        self.bg_task = self.bot.loop.create_task(self.post_meme())

    async def post_meme(self):
        'Posts a meme from r/dankmemes every hour'

        await self.bot.wait_until_ready()

        # Look for memes channel
        memes_channel = discord.utils.get(
            self.bot.get_all_channels(), name='memes')

        # Get guild
        for channel in self.bot.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                guild = channel.guild
                break

        # Check if the channel exists and it's a TextChannel
        if memes_channel is None or not isinstance(memes_channel, discord.TextChannel):
            memes_channel = await guild.create_text_channel('memes')

        while not self.bot.is_closed():
            meme_url = await self.fetch_meme()

            if meme_url is not None:
                print('Posting your hourly meme')
                await memes_channel.send(meme_url)
            else:
                print('Bot couldn\'t fetch a meme!')

            # Wait 1 hour
            await asyncio.sleep(60*60)

    async def fetch_meme(self):
        'Fetch post from reddit'

        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.reddit.com/r/dankmemes/new.json?limit=1') as r:
                if r.status == 200:
                    js = await r.json()
                    return js["data"]["children"][0]["data"]["url"]
                return None


def setup(bot):
    "Loads Bot Cog"
    bot.add_cog(AutoPosts(bot))
