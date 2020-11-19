from socket import *
ip_port = ('127.0.0.1',8000)
back_log = 5
buffer_size = 1024
tcp_server = socket(AF_INET,SOCK_STREAM)
#如果提示错误 Address already in use
# 在bind 前面加下面一行代码
# tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
while True:
    print('服务端开始运行')
    conn,addr = tcp_server.accept()  # 服务器阻塞在这里
    # print('双向连接是-->',conn)
    # print('客户端地址是-->',addr)
    while True:
        try:
            data = conn.recv(buffer_size)
            if not data:break
            print('客户端发来的消息-->',data.decode('utf-8'))
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
tcp_server.close()


