# 延时计算

class LazyProperty:
    def __init__(self,func):
        print("======>",func)
        self.func = func
    def __get__(self, instance, owner):
        print('get',instance,owner)
        #  instance 类   owner:实例 对象
        if instance is None:
            return self
        res = self.func(instance)
        # self.func.__name__  :函数名
        setattr(instance,self.func.__name__,res)
        return res
    # 如果定义了set 会变成数据描述符,数据描述符的优先级高于实例本身,重复调用r1.area方法时,会优先查找数据描述符自己,延时计算失效,
    # 没有定义set 是一个非数据描述符,优先级低于实例本身,调用r1.area 时将会先从实例本身查找area,存在则返回,不存在再去非数据描述中查找,实现延时计算功能

    # def __set__(self, instance, value):
    #     pass

class Room:

    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length
    # @property  # area = property(area)
    @LazyProperty
    def area(self):
        return "area==> 的返回值 %s" % (self.width * self.length)
        # return self.width * self.length
    @property # 静态属性 共实例去使用
    def area1(self):
        return "area1 的返回值 %s" %(self.width * self.length)

r1 = Room('别墅',1000,1000)
print(r1.area1)
# print(r1.area1)
# print(r1.area1)
print(r1.area)
print(r1.__dict__)
print(r1.area)
# print(r1.test)
# print(Room.test)
# print(Room.area)
# print(Room.__dict__)

