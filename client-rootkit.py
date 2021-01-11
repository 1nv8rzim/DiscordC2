from subprocess import Popen, PIPE
from socket import socket
from string import ascii_letters, digits
from os import getpid
from random import choice
from time import sleep

PROC_HIDE_CMD = ''
BEACON_INTERVAL = 0

token = ''.join(choice(ascii_letters + digits) for _ in range(72))
pid = getpid()

while True:
    if input == "exit":
        break
