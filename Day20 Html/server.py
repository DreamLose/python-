import socket
def main():
    sk = socket.socket()
    sk.bind(('127.0.0.1',8088))
    sk.listen(5)
    while True:
        conn,addr = sk.accept()
        buf = conn.recv(1024)
        f = open('表单标签.html','rb')
        data = f.read()

        conn.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n','utf-8'))
        conn.sendall(data)
        conn.close()

if __name__ == '__main__':
    main()