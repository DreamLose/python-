import socket
import time
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8800))
while True:
    inp = input('>>>>>:').strip()
    sk.send(inp.encode('utf-8'))
    data = sk.recv(1024)
    print(str(data,'utf-8'))
