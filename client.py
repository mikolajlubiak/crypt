#!/usr/bin/env python

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from time import sleep
from subprocess import check_call
from sys import argv, executable
try:
    from cryptography.fernet import Fernet
except:
    check_call((executable, '-m', 'pip', 'install', 'cryptography'))
    from cryptography.fernet import Fernet

class client():
    s = socket(AF_INET, SOCK_STREAM)

    def __init__(self):
        if len(argv) == 4: k = argv[3].encode()
        else:
            k = Fernet.generate_key()
            print(k).decode()
        self.f = Fernet(k)
        self.s.connect((argv[1], int(argv[2])))

    def sMsg(self, msg):
        self.s.send(self.f.encrypt(msg.encode()))

    def rMsg(self):
        while True:
            d = ''
            d = self.f.decrypt(self.s.recv(1024)).decode()
            print(end=d)
            sleep(0.1)

    def chat(self):
        receiving = Thread(target=self.rMsg)
        receiving.daemon = True
        receiving.start()
        while True:
                msg = input()
                msg = f"\nClient: {msg}\n"
                print(msg)
                self.sMsg(msg)

if __name__ == '__main__':
    check_call('clear')
    Client = client()
    Client.chat()
