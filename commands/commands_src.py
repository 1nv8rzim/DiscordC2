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

        # return output
        return output
    except:
        # return usage
        return parser.format_help()


async def echo(message):
    # creates parser
    parser = argparse.ArgumentParser(prog='echo', description='repeats input')
    parser.add_argument(
        'string', help='line to be repeated', type=str, nargs='+')
    try:
        # parse commandline inputs
        with hidePrint():
            args = parser.parse_args(message.content.split()[1:]) if len(
                message.content.split()) > 1 else parser.parse_args([])

        # returns output
        return ' '.join(args.string)
    except:
        return parser.format_help()


async def clear(message):
    # creates parser
    parser = argparse.ArgumentParser(prog='clear', description='clears lines')
    parser.add_argument('limit', default=150, type=positive_int, nargs='?',
                        help='number of previous lines to be clear [0,infinity)')
    try:
        with hidePrint():
            args = parser.parse_args(message.content.split()[1:]) if len(
                message.content.split()) > 1 else parser.parse_args([])
        await message.channel.purge(limit=args.limit + 1)
    except:
        return parser.format_help()


async def hello(message):
    return f'Hello {message.author.mention}!'


# helper fucntion
def positive_int(value):
    try:
        value = int(value)
    except:
        raise argparse.ArgumentTypeError()
    if value <= 0:
        raise argparse.ArgumentTypeError()
    return value
