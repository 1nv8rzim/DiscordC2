from datetime import datetime


def time(message):
    if '-v' in message.content or '--verbose' in message.content:
        if '-m' in message.content or '--military' in message.content:
            return datetime.now().strftime('%A, %B %d, %Y, %H:%M:%S')
        return datetime.now().strftime('%A, %B %d, %Y, %I:%M:%S %p')
    if '-m' in message.content or '--military' in message.content:
        return datetime.now().strftime("%H:%M:%S")
    return datetime.now().strftime("%I:%M:%S %p")


def echo(message):
    try:
        return message.content.split(' ', 1)[1]
    except:
        return ''


async def clear(message):
    try:
        limit = int(message.content.split('', 1)[1])
        await message.channel.purge(limit)
    except:
        await message.channel.purge(limit=100)
