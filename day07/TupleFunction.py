# 元组,元素不可被修改，不能被增加或者删除，元组内的列表可以修改
# 一般写元组的时候，推荐最后加入"，"
tu = (111, 222, 545, 3333, 222,)
v = tu.count(222)
# 获取指定元素的index
v = tu.index(111)
print(v)
print(v)
# 索引
print(tu[0])
# 切片
print(tu[0:-1])
# 转换
s = "qwqw"
li = ["ds",21212]
tu = (2323,"dsdw",)
print(tuple(s))
print(tuple(li))
print(list(tu))
v = li.extend(tu)
print(v,li)
