from socket import *
import subprocess
import struct
ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024
tcp_service = socket(AF_INET,SOCK_STREAM)
tcp_service.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_service.bind(ip_port)
tcp_service.listen(back_log)
while True:
    con,addr = tcp_service.accept()
    print('新的客户端连接-->',addr)
    while True:
        cmd = con.recv(buffer_size)
        print('收到客户端命令-->',cmd)
        if not cmd:break
        # 将运行结果交给管道,执行命令,得到运行结果
        res = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # 从管道读取内容
        err = res.stderr.read() # 错误的管道中没有内容,代表输入正确
        if err:
            cmd_res = err
        else:
            cmd_res = res.stdout.read()
        # 发送
        if not cmd_res:
            cmd_res = "execute success".encode('UTF-8')
        lenth = len(cmd_res)
        data_l = struct.pack('i',lenth)
        # 发送长度
        con.send(data_l)
        # 发送内容
        con.send(cmd_res)
    con.close()
tcp_service.close()
