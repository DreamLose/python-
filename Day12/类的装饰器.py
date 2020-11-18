def Deco(obj):
    print("======",obj)
    obj.x=1
    obj.y = 2
    return  obj
# @Deco   # test = Deco(test)
# def test():
#     print("运行")
#
# test()
# print(test.__dict__)
@Deco  # Foo = Deco(Foo)
class Foo:
    pass
f1 = Foo()
print(Foo.__dict__)
print(f1.__dict__)
