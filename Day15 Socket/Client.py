import socket
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('192.168.0.101',8000)) # 拨通
phone.send("hello".encode('utf-8')) # 发送消息
msg = phone.recv(1024) # 接收消息
print(' 收到服务端发来的消息->',msg)