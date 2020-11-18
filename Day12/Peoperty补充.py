"""
方式一:
class Foo:
    @property
    def test(self):
        print('get的时候运行我')
    @test.setter
    def test(self,val):
        print('set的时候运行我',val)
    @test.deleter
    def test(self):
        print('删除的时候运行我')
"""
# 方式二
class Foo:

    def set_test(self):
        print('get的时候运行我')


    def get_test(self, val):
        print('set的时候运行我', val)


    def del_test(self):
        print('删除的时候运行我')
    #     注意, set_test,get_test,del_test 顺序不能变
    test = property(set_test,get_test,del_test)

f1 = Foo()
f1.test
f1.test = "aaa"
del f1.test