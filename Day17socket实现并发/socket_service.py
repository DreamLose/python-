from socket import *
import subprocess
import struct
import socketserver
ip_port = ('127.0.0.1',8080)
buffer_size = 1024
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn-->',self.request)  # conn
        print('addr-->',self.client_address) # addr
        while True:
            try:
                # 收消息
                data = self.request.recv(buffer_size)
                if not data:break
                print('收到客户端信息-->',data)
                # 发消息
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break
if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(ip_port,MyServer) #多线程
    # s = socketserver.ForkingTCPServer(ip_port,MyServer)  #多进程(开销大)
    s.serve_forever()



#

# back_log = 5
# buffer_size = 1024
# tcp_service = socket(AF_INET,SOCK_STREAM)
# tcp_service.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# tcp_service.bind(ip_port)
# tcp_service.listen(back_log)
# while True:
#     conn,addr = tcp_service.accept()
#     print('接入的客户端是-->',addr)
#     while True:
#         data = conn.recv(buffer_size)
#         if not data:break
#         print("收到客户端信息-->", data.decode('utf-8'))
#         res = subprocess.Popen(data.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
#         err_msg = res.stderr.read()
#         if err_msg:
#             back_msg = err_msg
#         else:
#             back_msg = res.stdout.read()
#         m_length = len(back_msg)
#         res = struct.pack('i',m_length)
#         conn.send(res)
#         conn.send(back_msg)
#     conn.close()
# tcp_service.close()
#

