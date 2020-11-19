l = ['a','e','b','c','d']
def test():
    return l.pop()
#
x = iter(test,'e')
print(x.__next__())
print(x.__next__())
#偏函数
from functools import partial

def add(x,y):
    print('x-->%s,y-->%s' %(x,y))
    return x+y
func = partial(add,1)
print(func(1))
print(func(2))

# recv_size = 0
# recv_msg = b''
# while recv_size < length:
#     recv_msg += tcp_clent.recv(buffer_size)
#     recv_size = len(recv_msg)
# print(recv_msg.decode('UTF-8'))

# partial(tcp.clent.recv,1024)
