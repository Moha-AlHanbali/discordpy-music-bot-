"""This module plays the following song in a queue"""

import discord
import asyncio


async def play_next(bot, queue, voice_channel, message):
    """
    play_next allows bot to play next track in a queue.

        Arguments:
            bot: MusicBot instance
            queue: MusicBot track queue
            voice_channel: VoiceChannel Instance
            message: Message instance

        Return:
            Sends a status message
    """

    queue.pop(0)
    if queue:

        voice_channel.play(discord.FFmpegPCMAudio(queue[0]['url']) , after = lambda e: asyncio.run_coroutine_threadsafe(play_next(bot, queue, voice_channel, message), bot.loop))
        return  await message.channel.send(f'Started Playing {queue[0]["title"]}!')

    return await message.channel.send(f'Queue ended!')
