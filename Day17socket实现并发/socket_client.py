from socket import *
import struct

ip_port = ('127.0.0.1',8080)
buffer_size = 1024
tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input(">>>:").strip()
    if not msg: continue
    if msg == 'quit': break
    tcp_client.send(msg.encode('utf-8'))
    back_msg = tcp_client.recv(buffer_size)
    print('服务器返回信息-->',back_msg.decode('utf-8'))
tcp_client.close()