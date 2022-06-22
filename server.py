import socket, threading, time

class Server:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.s.bind(('127.0.0.1', 12345))
        self.s.listen(5)
        self.client, self.addr = self.s.accept()

    def rMsg(self):
        while True:
            d = ''
            d = self.client.recv(1024).decode()
            print(end=d)
            time.sleep(0.1)

    def chat(self):
        self.receiving = threading.Thread(target=self.rMsg)
        self.receiving.daemon = True
        self.receiving.start()
        while True:
            msg = input()
            msg = f"\nADMIN: {msg}\n"
            print(msg)
            self.client.send(msg.encode())

if __name__ == '__main__':
    Server_m = Server()
    Server_m.chat()
    Server_m.receiving.join()
    Server_m.s.close()
