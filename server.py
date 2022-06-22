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

class Server:
    s = socket(AF_INET, SOCK_STREAM)

    def __init__(self):
        if len(argv) == 4: k = argv[3].encode()
        else:
            k = Fernet.generate_key()
            print(k.decode())
        self.f = Fernet(k)
        self.s.bind((argv[1], int(argv[2])))
        self.s.listen(3)
        self.client, self.addr = self.s.accept()

    def rMsg(self):
        while True:
            d = ''
            d = self.f.decrypt(self.client.recv(1024)).decode()
            print(end=d)
            sleep(0.1)

    def chat(self):
        self.receiving = Thread(target=self.rMsg)
        self.receiving.daemon = True
        self.receiving.start()
        while True:
            msg = input()
            msg = f"\nADMIN: {msg}\n"
            print(msg)
            self.client.send(self.f.encrypt(msg.encode()))

if __name__ == '__main__':
    check_call('clear')
    Server_m = Server()
    Server_m.chat()
    Server_m.receiving.join()
    Server_m.s.close()
