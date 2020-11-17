class Foo:
    def __call__(self, *args, **kwargs):
        print('实例执行了')
f1 = Foo()
# f1.__call__()
f1()  # 调用了Foo下的__call__()

