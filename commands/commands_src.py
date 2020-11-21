from datetime import datetime
import argparse
from contextlib import contextmanager
import sys
import os
from commands import commands


# essential functions

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


def get_args(parser, message):
    if message is 'help':
        return parser.format_help()
    with hidePrint():
        return parser.parse_args(message.content.split()[1:]) if len(
            message.content.split()) > 1 else parser.parse_args([])


# commands

async def info(message):
    pass


async def show(message):
    pass


async def c2(message):
    pass


async def upload(message):
    pass


async def help(message):
    # creates parser
    parser = argparse.ArgumentParser(
        prog='help', description='helps learn more about functions')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increases verbosity of output')
    parser.add_argument('command', default=None, nargs='?',
                        help='commands to provide help on')

    try:
        # parses commandline inputs
        args = get_args(parser, message)

        # get requested help
        for cmd in args.command:
            if cmd in commands:
                commands[cmd]('help')

        # if not help is requested, help for all functions is given
        if args.commands is None:
            for cmd in commands:
                commands[cmd]('help')
    except:
        # return usage
        return parser.format_help()


async def console(message):
    pass


async def time(message):
    # creates parser
    parser = argparse.ArgumentParser(prog='time', description='gets time')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increases verbosity of output')
    parser.add_argument('-m', '--military', action='store_true',
                        help='displays time in military time')

    try:
        # parses commandline inputs
        args = get_args(parser, message)

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

        # returns output
        return output
    except:
        # returns usage
        return parser.format_help()


async def echo(message):
    # creates parser
    parser = argparse.ArgumentParser(prog='echo', description='repeats input')
    parser.add_argument(
        'string', help='line to be repeated', type=str, nargs='+')
    parser.add_argument('-n', help='number of times repeated',
                        default=1, type=number_filter(lambda x: x > 0))
    try:
        # parse commandline inputs
        args = get_args(parser, message)

        # returns output
        msg = ' '.join(args.string)
        for i in range(args.n):
            await message.channel.send(msg)
    except:
        # returns usage
        return parser.format_help()


async def clear(message):
    # creates parser
    parser = argparse.ArgumentParser(prog='clear', description='clears lines')
    parser.add_argument('limit', default=150, type=number_filter(lambda x: x >= 0), nargs='?',
                        help='number of previous lines to be clear [0,infinity)')
    try:
        # parse commandline inputs
        with hidePrint():
            args = get_args(parser, message)

        # purges desired lines
        await message.channel.purge(limit=args.limit + 1)
    except:
        # return usage
        return parser.format_help()


async def hello(message):
    # creates parser
    parser = argparse.ArgumentParser(
        prog='hello', description='says hello to user')

    try:
        # parse commandline inputs
        with hidePrint():
            args = get_args(parser, message)

        # return output
        return f'Hello {message.author.mention}!'
    except:
        # returns usage
        return parser.format_help()


# helper functions

def number_filter(function):
    def inner(value):
        try:
            value = int(value)
        except:
            raise argparse.ArgumentTypeError()
        if not function(value):
            raise argparse.ArgumentTypeError()
        return value
    return inner
