class Foo:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n == 20:
            raise StopIteration('终止了')
        self.n +=1
        return self.n

f1 = Foo(10)
# print(f1.__next__())
# print(f1.__next__())
# print(next(f1))
# for i in f1:
#     print(i)


# 斐波那契数列
# 1 1 2 3 5 8 13 21

class Fibl:
    def __init__(self):
        self._a = 1
        self._b = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self._a > 150:
            raise StopIteration('终止了')
        self._a,self._b =self._b,self._a + self._b
        return self._a

fi = Fibl()
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print('=============')
for i in fi:
    print(i)