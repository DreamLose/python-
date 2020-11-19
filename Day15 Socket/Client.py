import socket
ip_port = ('127.0.0.1',8000)
buffer_size = 1024
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(ip_port) # 拨通
while True:
    msg = input(">>>>:").strip()
    if not msg:continue
    phone.send(msg.encode('utf-8'))
    print('客户端已经发送消息')
    data = phone.recv(buffer_size)
    print('收到服务端发来的消息-->',data.decode('utf-8'))
phone.close()