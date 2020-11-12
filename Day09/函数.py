# 函数
# 返回值个数 0  ： 返回none；
# 返回值个数 1  ： 返回object
# 返回值格式 >1 :  返回tuple
def test():
    x = 3
    y = x*5 +10
    return y
print(test())

#参数组 ： **字典 * 列表
def testFunc(x,*args):
    print(x)
    print(args)
testFunc(1,23,4,5,6,7,8)
testFunc(1,[3,3,23,23,3,42,423])
testFunc(1,*{1,21,2,12,432,432,"dsdsd"})
testFunc(1,{"name":"alex"})
testFunc(1)
def testFunc1(x,**kwargs):
    print(x)
    print(kwargs)
testFunc1(1,y=2,z=3)
# testFunc1(1,{"eww":"dw"}) #报错
testFunc1(1,**{"eww":"dw"})
def testFunc2(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)

