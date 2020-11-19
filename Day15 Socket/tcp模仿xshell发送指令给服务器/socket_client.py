from socket import *
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
    cmd_res = tcp_clent.recv(buffer_size)
    print(cmd_res.decode('UTF-8'))
tcp_clent.close()