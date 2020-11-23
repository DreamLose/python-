# 同步
# 异步
# 阻塞
# 非阻塞
#



"""
######################io非阻塞
"""

# import socket
# import time
# sk = socket.socket()
# sk.bind(('127.0.0.1',8800))
# sk.listen(5)
#
# # 设置了这一句变成 非阻塞IO,不会等待客户端连接
# sk.setblocking(False)
# while True:
#     try:
#         conn,addr = sk.accept()
#         print("+++++",addr)
#         client_msg = conn.recv(1924)
#         print(str(client_msg,'utf-8'))
#         conn.close()
#     except Exception as e:
#         # 这里可以写其他逻辑,不用等待客户端连接,一旦发现客户端发来的信息,便会返回去处理消息
#         print(e)
#         time.sleep(4)
#
# # 缺点:不能及时处理收到的数据,发了太多系统调用

"""
######################io多路复用
三种方式:
    select ,最大监听连接数 1024 个 ,每次都要轮询才能知道哪个客户端发送的消息
    poll , 最大监听连接数 没有限制
    epoll, 每次客户端发消息 都要自报家门,少了轮询步骤,提高效率

触发方式
1.水平触发:只有高电平(1)或者低电平(0)的时候才触发,只要在这两种状态就能得到通知,
   1 ---------------                  -------------------

   0                ------------------
   只要在(1)或者(0)的时候触发
2.边缘触发:只有电平发生变化(高电平到低电平,或者低电平到高电平)的时候才触发通知

"""
# import socket
# import select
# sk = socket.socket()
# sk.bind(('127.0.0.1',8800))
# sk.listen(5)
# inp= [sk,]
# while True:
#     # select.select(input,output,errput,监听轮训时间)
#
#     # 当有客户端连接进来的时候,sk会有变化,
#     # 当客户端发送消息的时候,conn会有变化
#     r,w,e = select.select(inp,[],[],5)  #水平触发
#     for i in r:
#         conn,addr = i.accept()
#         print(conn)
#         inp.append(conn)
#         data = conn.recv(1024)
#         print(str(data,'utf-8'))
#     print('>>>>>>>>>')

"""
######################io异步   全程无阻塞
"""