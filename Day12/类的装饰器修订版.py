def Typed(**kwargs):
    def Deco(obj):
        print("---->", kwargs)
        print("======>",obj)
        # obj.x=1
        # obj.y = 2
        for key,value in kwargs.items():
            setattr(obj,key,value)
        return  obj
    print("==>",kwargs)
    return Deco

@Typed(x=1,y=2,z=3)  #  Typed(x=1,y=2,z=3)--->Deco  2 @Deco --> Foo = Deco(Foo)
class Foo:
    pass
f1 = Foo()
print(Foo.__dict__)
# print(f1.__dict__)
@Typed(name="诸葛亮")
class Bar():
    pass
print(Bar.__dict__)
print(Bar.name)