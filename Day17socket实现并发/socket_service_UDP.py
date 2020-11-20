from socket import *
import subprocess
import struct
import socketserver
ip_port = ('127.0.0.1',8800)
buffer_size = 1024
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('request-->',self.request)
        data = self.request[0]
        print('收到客户端消息-->',data)
        self.request[1].sendto(data.upper(),self.client_address)
        #
        # print('addr-->',self.client_address) # addr
if __name__ == '__main__':
    s = socketserver.ThreadingUDPServer(ip_port,MyServer) #多线程
    # s = socketserver.ForkingTCPServer(ip_port,MyServer)  #多进程(开销大)
    s.serve_forever()




