s = set('hello')
print(s)
s = {1,2,3,4,5,6,23,4}
# add
s.add('32')
print(s)
s.add(3)
print(s)
# s.clear()
# print(s)
s1 = s.copy()
print(s)
# pop() 随机删除
s.pop()
print(s)
# remove(); 指定删除，删除不存在的项会报错
s.remove('32')
print(s)
# discard() 删除元素，不存在的元素删除不报错
s.discard(3)
print(s)


ls1 = ["小蓝",'小红','xiaocang','小明']
ls2 = ['小蓝','小吕','xisozhu']
# 共同部分关系测试
ps = set(ls1)
ps2 = set(ls2)
print(ps,ps2)
# 获取共同部分 intersection()
print(ps.intersection(ps2))
print(ps&ps2)
# 并集 union()
print(ps.union(ps2))
print(ps|ps2)
# 差集 difference()
print(ps.difference(ps2))
print(ps-ps2)
print("--------")
print("初始：",ps)
print("初始ps2：",ps2)

# 集合其他运算
# 交叉补齐
print(ps.symmetric_difference(ps2))
print(ps^ps2)
# 交叉补齐，并且赋值给ps
ps.symmetric_difference_update(ps2)
print("--------")
print("结束：",ps)
print("--------")

s1 = {1,2,3}
s2 = {2,3}
#isdisjoint() 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 Fals
print(s2.isdisjoint(s1))
# issubset() 判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False
# s2 是否是s1 的子集
print(s2.issubset(s1))
# s1 是否是s2 的父集
print(s1.issuperset(s2))
# 更新多个值
s1.update(s2)
print(s1)
# 合并并且不会重新赋值，不是更新
print(s1.union(s2))

# 不可变集合
sss = frozenset("hellp")
print(sss)




