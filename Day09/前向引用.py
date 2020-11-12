
def foo():
    print("foo")
    bar()
def bar():
    print("bar")
foo()
name = 'ddd'
def tes():
    name = "dsdsdsd"
    def tres():
        name = "xioga"
        def tt():

            print(name)
        return tt
    return tres
res = tes()
res()()

"""
=============  递归函数
"""
def calc(n):
    print(n)
    if n>0:
        calc(n-1)
    else:
        return
calc(10)

# 匿名函数
y = lambda x:x+1
print(y(10))
name = "alex"
func = lambda x : x + "_sb"
print(func("alex"))


