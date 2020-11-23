import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock,mask):
    conn,addr = sock.accept()
    print('accepted',conn,'from',addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    data = conn.recv(1024)
    if data:
        print('echoing',repr(data),'to',conn)
        conn.send(data)
    else:
        print('closing',conn)
        sel.unregister(conn)
        conn.close()
sock = socket.socket()
sock.bind(('127.0.0.1',8800))
sock.listen(5)

# 设置非阻塞
sock.setblocking(False)
# 注册 绑定accept
sel.register(sock,selectors.EVENT_READ,accept)

# 真正监听
while True:
    events = sel.select()
    print(events)
    for key,mask in events:
        # key.data--> accept
        # key.fileobj -->sock
        print('key--->',key)

        print('mask--->',mask)
        callBack = key.data
        print('callBack--->', callBack)
        callBack(key.fileobj,mask)