from multiprocessing import Process,Pipe

def f(conn):
    conn.send([12,{'name':"貂蝉"},'hello'])
    response = conn.recv()
    print("response--->",response)
    conn.close()
    print('q_ID2:',id(conn))

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    print('q_ID1:', id(child_conn))
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send('儿子你好')

    p.join()
    print('end.....')

