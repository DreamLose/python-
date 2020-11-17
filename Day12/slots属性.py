class Foo:
    '我是描述信息,不能被子类继承'
    # __slots__ = ['name','age']  #['name':None,'age':None]
    __slots__ = "name"  #可以节省内存,缺点是不可以新增属性,没有了__dict__属性
f1 = Foo()  #产生的实例不在具有__dict__ ,每个实例只能设置一个name的属性
f1.name = "小鲁班"
print(f1.name)
# f1.age =18  # setattr --> f1.__dict__['age'] = 18
# print(f1.age)
# f1.__dict__  不存在了
print(f1.__slots__)
print(Foo.__slots__)
f2 = Foo()
print(f2.__slots__)
# print(f2.__dict__)


class Food(Foo):
    pass

print(Foo.__doc__)
print(Food.__doc__)

print(Food.__dict__)