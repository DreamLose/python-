from socket import *

ip_port = ('127.0.0.1', 8080)
buffer_size = 1024
# SOCK_DGRAM 数据报  基于udp
udp_client = socket(AF_INET, SOCK_DGRAM)
while True:
    msg = input(">>>:").strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)
    data,addr = udp_client.recvfrom(buffer_size)
    print('ntp服务器的标准时间是-->',data.decode('utf8'))
udp_client.close()