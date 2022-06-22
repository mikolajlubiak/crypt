import socket, time, threading

class client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.s.connect(('127.0.0.1', 12345))

    def sMsg(self, msg):
        self.s.send(msg.encode())

    def rMsg(self):
        while True:
            d = ''
            d = self.s.recv(1024).decode()
            print(end=d)
            time.sleep(0.1)

    def chat(self):
        receiving = threading.Thread(target=self.rMsg)
        receiving.daemon = True
        receiving.start()
        while True:
                msg = input()
                msg = f"\nClient: {msg}\n"
                print(msg)
                self.sMsg(msg)

if __name__ == '__main__':
    Client = client()
    Client.chat()
