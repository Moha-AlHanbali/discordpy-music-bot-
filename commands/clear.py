"""This module clears the track queue."""

async def clear(queue, message):
    """
    clear empties MusicBot track queue.

        Arguments:
            queue: MusicBot track queue

        Return:
            Modified queue
            
    """
    if not queue:
        await message.channel.send('Queue is already empty!')
    else:
        queue = []
        await message.channel.send('Cleared queue!')
    return queue
    