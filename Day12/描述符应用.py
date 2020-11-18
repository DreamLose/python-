# 增加属性类型限制 限制People 中的name 属性只能是str age属性只能是 int

# 数据描述符
class Typed():
    def __init__(self,key,exceptipnType):
        self.key = key
        self.exceptipnType=exceptipnType
    def __get__(self, instance, owner):
        print('**get方法***')
        # print('**instance参数 [%s] ***' %instance)
        # print('**owner参数 [%s] ***' %owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('**set方法***')
        # print('**instance参数 [%s] ***' %instance)
        # print('**value参数 [%s] ***' %value)
        # 进行逻辑判断,如果不是字符串,返回数据不合规
        if not isinstance(value,self.exceptipnType):
            print('你的数据不符合')
            raise TypeError('%s 传入的数据不是%s' %(self.key,self.exceptipnType))
            # return
        instance.__dict__[self.key] = value
    def __delete__(self, instance):
        print('**delete方法***')
        instance.__dict__.pop(self.key)


class People:
    name = Typed('name',str)
    age = Typed('age',int)
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1 = People('安其拉',18,3000)
# print(p1.__dict__)
# print(p1.name)
p1.name = '妲己'
# print(p1.name)
#
# # print(p1.__dict__)
# del  p1.name
# print(p1.__dict__)
p2 = People(1212,18,3000)
# print(p2.__dict__)