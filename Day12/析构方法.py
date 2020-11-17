class Foo:
    def __init__(self,name):
        self.name =name
    def __del__(self): # 函数回收的时候调用,释放内存
        print("我是析构函数")


f1 = Foo('程咬金')
# del f1
# print('-------------------')
del f1.name
print('-------------------')

