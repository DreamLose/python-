class Foo:
    def __init__(self,name,mode='r',encoding='urt-8'):
        self.name=name
    def __enter__(self):
        print('__enter__')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        print("exc_type",exc_type)  # 异常类型
        print("exc_val", exc_val)  #异常信息
        print("exc_tb", exc_tb) #异常追踪 d
        return True  # 返回Ture 程序不会终止 with中的代码不会再执行

with Foo('a.txt') as f:
    print(f)
    print(dafsadfsds)
    print(f.name)
    print("==========>")



print("结束====================")