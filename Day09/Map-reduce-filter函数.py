"""
map() 处理一个可迭代的序列中的每个元素，得到的结果是一个"列表"，该列表元素个数以及位置与原来一样
filter() 用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
reduce() 会对参数序列中元素进行累积
"""
#map 函数 处理结束后还是个列表
numl = [1,2,3,4,3,1,3,4,2,4,2]
res = map(lambda x : x+1,numl)
print(res)
print(list(res))
for i in res:
    print(i)

stra = "ldldld"
print(list(map(lambda x : x.upper(),stra)))
# filter 函数  过滤
personList = ["xiaoss_sss","dsdsd_sss","jfwjfiw_sss","dsfa"]
res = filter(lambda x : not x.endswith("_sss"),personList)
print(list(res))

# reduce 函数 python3 要导入 reduce 模块
# reduce 函数 合并一个数列
from functools import reduce
numl = [1,100,12]

res = reduce(lambda x,y=0 : y + x,numl,1)
print(res)
