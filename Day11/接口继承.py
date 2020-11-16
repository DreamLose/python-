import abc
# 基类只是为了规范化子类
class All_file(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        '子类必须实现读功能'
        pass
    @abc.abstractmethod
    def write(self):
        '子类必须实现写功能'
        pass
class Text(All_file):
    def read(self):
        print("文本数据读取方法")
    def write(self):
        print("文本数据写入方法")

class Disk(All_file):
    def read(self):
        print("硬盘数据读取方法")
    def write(self):
        print("硬盘数据写入方法")

d = Disk()
d.read()


# 多继承顺序
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B):
    pass
class E(C):
    pass
class F(D,E):
    pass
# 查找顺序 python3 中 只用新式类
print(F.mro())  # 新式类中才有

# python2 中
# 经典类
# class A:
#     pass
# 新式类
# class A(object):
#     pass