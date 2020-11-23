import socket
import select
sk = socket.socket()
sk.bind(('127.0.0.1',8800))
sk.listen(5)
inp= [sk,]
while True:
    # select.select(input,output,errput,监听轮训时间)
    r,w,e = select.select(inp,[],[],5)  #水平触发
    for obj in r:
        if obj == sk:
            conn,addr = obj.accept()
            print(conn)
            inp.append(conn)
        else:
            data = obj.recv(1024)
            if data:
                print(str(data,'utf-8'))
                res = input('回答%s客户>>>:' %inp.index(obj))
                obj.sendall(res.encode('utf-8'))
            else:
                inp.remove(obj)
   
