from subprocess import Popen, PIPE
from socket import socket
from string import ascii_letters, digits
from os import getpid
from random import choice

token = ''.join(choice(ascii_letters + digits) for _ in range(72))
pid = getpid()
