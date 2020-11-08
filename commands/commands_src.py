from datetime import datetime
import argparse
from contextlib import contextmanager
import sys
import os


class hidePrint:
    def __enter__(self):
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr


async def temp(message):
    return None


async def time(message):
    # creates parser
    parser = argparse.ArgumentParser(prog='time', description='gets time')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increases verbosity of output')
    parser.add_argument('-m', '--military', action='store_true',
                        help='displays time in military time')

    try:
        # parses commandline inputs
        with hidePrint():
            args = parser.parse_args(message.content.split()[1:]) if len(
                message.content.split()) > 1 else parser.parse_args([])

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
        return parser.format_help()


async def echo(message):
    # creates parser
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
