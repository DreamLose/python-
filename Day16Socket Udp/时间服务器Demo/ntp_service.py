from socket import *
import time
ip_port = ('127.0.0.1',8080)
buffer_size = 1024
# SOCK_DGRAM 数据报  基于udp
udp_service = socket(AF_INET,SOCK_DGRAM)
udp_service.bind(ip_port)

while True:
    data,addr = udp_service.recvfrom(buffer_size)
        # print(data)
    back_time = time.strftime("%Y-%m-%d %X")
    udp_service.sendto(back_time.encode('utf-8'),addr)
udp_service.close()