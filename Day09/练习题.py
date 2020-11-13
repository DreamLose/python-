# 1 bool值为False的情况
"""
print(bool(0))
print(bool(False))
print(bool(""))
print(bool([]))
print(bool([]))
print(bool(()))
print(bool(None))
print(bool({}))


def sumNu(start,end):
    sumM = 0
    for i in range(start,end):
        if i%3 == 0 and i%7 == 0:
            sumM +=i
    return sumM
# 递归方法
def func(start,end,a=0):
    if start == end:
        return a
    if start%3 == 0 and start%7 == 0:
        a += start
    start +=1
    ret = func(start,end,a)
    return ret
res = func(1,100)
print(res)

l1 = [11,22,33]
l2 = [22,33,44]
s1 = set(l1)
s2 = set(l2)
# s = s1&s2
s = s1.intersection(s2)
print(s)

# 内存地址改变
x = 1
print(id(x))
x = 2
print(id(x))

def strT(s):
    ret = {'l':0,'L':0,'s':0,'o':0}
    for i in s:
        if ord('a') <= ord(i) and ord(i) <= ord('z'):
            ret["l"] +=1
        elif ord('A') < ord(i) and ord(i) < ord('Z'):
            ret["L"] += 1
        elif ord('0') < ord(i) and ord(i) < ord('9'):
            ret["s"] += 1
        else:
            ret['o'] +=1
    return ret

res = strT("212weweWQE212@@")
print(res)
def func(x,*y,**z):
    print(x,y,z)
# **z : 传值只能通过 name = 'alex' 键值对、或者**{'name':'alex'}
func(1,[1,2,3,4],name=2,age=4)#1 ([1, 2, 3, 4],) {'name': 2, 'age': 4}
func(1,*[1,2,3,4],name=2,age=4) #1 (1, 2, 3, 4) {'name': 2, 'age': 4}
func(1,*[1,2,3,4],{'name':'alex','age':13}) #1 (1, 2, 3, 4, {'name': 'alex', 'age': 13}) {}
#
s= "哈哈"
print(s.encode("utf-8"))
a = bytes(s,'utf-8')
print(a)

l1 = ["al",1,2,3,2]
l2 = ["is",1,2,3,2]
l3 = ["good",1,2,3,2]
l4 = ["boy",1,2,3,2]
print("_".join(list(zip(l1,l2,l3,l4))[0]))

def f1(agr):
    print(id(agr))
n = 111111
print(id(n))
f1(n)
"""
#
# 10 ==>1
# 9  ==> 4
# 8  ==> 10
#
# def func(x,n=1):
#     for i in range(1,10):
#         n = (n + 1) *2
#     return n
# print(func(10))

# def func(x,y=0):
#     y += 1
#     if y == 5:
#         return x + y
#     x += y
#     func(x,y)
#     x +=y
#     return x
# num = 1
# result = func(num)
# print(num)
# print(result)

def test():
    for i in range(4):
        yield i
t = test()
t1 = (i for i in t)
t2 = (i for i in t1)
print(list(t2))
print(list(t1))
