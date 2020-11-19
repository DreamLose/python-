from socket import *
ip_port = ('127.0.0.1',8000)
buffer_size = 1024
# SOCK_DGRAM 数据报  基于udp
udp_service = socket(AF_INET,SOCK_DGRAM)
udp_service.bind(ip_port)

while True:
    data,addr = udp_service.recvfrom(buffer_size)
    print(data)
    udp_service.sendto(data.upper(),addr)
udp_service.close()