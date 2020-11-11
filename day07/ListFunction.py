li = [1, 12, "age", "alex", ["lilei", "wangmei", "小明"]]
# 索引
print(li[2])
# 切片
print(li[3:5])
print(li[2:-1])
# 修改
li[3] = 130
li[1:3] = [120,90]
print("-------------\n",li)
# 删除
# 通过索引删除
del li[1]
print("-------------\n",li)
# 通过切片删除
del li[2:3]
print("-------------\n",li)
# in 操作
v = 90 in li
print("-------------\n",v)
v = "wangmei" in li
print("-------------\n",v)
print(li[2][0])
"""
==================== 列表 ============
"""
# 字符串转list
s = "分身乏术发方式发我dafd"
v = list(s)
print("-------------\n",v)
# 列表转字符串,如果列表中只有字符串，直接使用join方法
li = ["alex","age","age"]
newlist = "_".join(li)
print(newlist)
# append() 追加 原来值最后追加
v = li.append("新加")
print("--------\n",v)
print("--------\n",li)
# clear() 清空列表
# li.clear()
# print("--------\n",li)
# copy() 浅拷贝
v = li.copy()
# count() 计算元素出现的次数
v = li.count("age")
print("--------\n",v)
#extend() 扩展原列表
li.extend([3232,"不得了"])
li.extend("不得了")
li.append(["新加","appen"])
print("--------\n",li)
# index()  根据值获取当前索引位置，从左开始找
v = li.index("age")
print(v)
# insert() 指定索引位置插入
li.insert(0,99)
print(li)
#pop() 删除某个值，并获取删除的值,默认最后一个
v = li.pop()
print("--------\n")
print(li)
print(v)
li.pop(1)
print("--------")
print(li)
print(v)
# remove() 删除列表中的指定值 左边优先
li.remove("age")
print(li)
# reverse() 当前列表反转
li.reverse()
print(li)
# sort() 排序
li = [11,9,23,98,0,2,9,5]
li.sort()
print(li)
# 从大到小排序
li.sort(reverse=True)
print(li)

tuple