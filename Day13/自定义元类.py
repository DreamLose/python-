class myType(type):
    def __init__(self,obj,supClass,args):
        print("元类的构造函数执行")
        print(obj,supClass,args)
    def __call__(self, *args, **kwargs):
        print("==========>",self)
        print(args,kwargs)
        obj = object.__new__(self) # object.__new__(Foo)->f1
        self.__init__(obj,*args,**kwargs)  #Foo.__init__(f1,*args,**kwargs)
        return obj
class Foo(metaclass=myType):  #myType('Foo',(object,),{})
    def __init__(self,name):
        self.name = name


f1 = Foo('alex')
print(f1)
print(f1.name)
print(f1.__dict__)
#
# def test(*args):
#     print(args)
#
# # test(**{'s':1})
