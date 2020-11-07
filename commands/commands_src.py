from datetime import datetime
import argparse


async def temp(message):
    return None


async def time(message):
    # parser
    parser = argparse.ArgumentParser(prog='time', description='gets time')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increases verbosity of output')
    parser.add_argument('-m', '--military', action='store_true',
                        help='displays time in military time')
    args = parser.parse_args(message.content.split()[1:]) if len(
        message.content.split()) > 1 else parser.parse_args([])

    try:
        # gets time
        time = datetime.now()

        # military time or not
        if args.military:
            output = time.strftime('%H:%M:%S')
        else:
            output = time.strftime('%I:%M:%S %p')

        # verbose output or not
        if args.verbose:
            output = time.strftime('%A, %B %d, %Y, ') + output

        return output
    except:
        pass


async def echo(message):
    try:
        return message.content.split(' ', 1)[1]
    except:
        return ''


async def clear(message):
    try:
        limit = int(message.content.split(' ', 1)[1]) + 1
        if limit < 0:
            raise Exception()
        await message.channel.purge(limit=limit)
    except:
        await message.channel.purge(limit=150)


async def hello(message):
    return f'Hello {message.author.mention}!'
