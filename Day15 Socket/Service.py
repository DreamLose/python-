# 三次握手 不涉及数据传输,只是建立连接
# 四次挥手 涉及数据,谁结束谁主动断开连接
import socket

#AF_INET : 基于网络
# STREAM TCP
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 初始化
phone.bind(('127.0.0.1',8000)) # 绑定自己ip,端口号
phone.listen(5)  # 开机 (半连接存储个数,半连接池)
print('====等电话====')
conn,addr = phone.accept() #等消息
print(addr)
conn.send('我可以接受消息了'.encode('utf-8'))
msg = conn.recv(1024)  #收消息
print('客户端发来的消息是-->',msg)
conn.send(msg.upper())  # 发消息
conn.close() # 关闭连接
phone.close() # 关闭
