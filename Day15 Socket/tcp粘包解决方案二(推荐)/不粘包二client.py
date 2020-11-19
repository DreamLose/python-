from socket import *
from functools import partial
import struct
ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024
tcp_clent = socket(AF_INET,SOCK_STREAM)
tcp_clent.connect(ip_port)
while True:
    cmd = input('>>>:').strip()
    if not cmd:continue
    if cmd == 'quit':break
    tcp_clent.send(cmd.encode('UTF-8'))
    print('发送成功---------')
    #  解决粘包地方

    # 获取内容长度
    length_data = tcp_clent.recv(4)
    length = struct.unpack('i',length_data)[0]
    recv_size = 0
    recv_msg = b''
    while recv_size < length:
        recv_msg += tcp_clent.recv(buffer_size)
        recv_size = len(recv_msg)
    print(recv_msg.decode('UTF-8'))

    # recv_msg = ''.join(iter(partial(tcp_clent.recv, buffer_size), b''))
    # print(recv_msg.decode('UTF-8'))
tcp_clent.close()