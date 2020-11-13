def getPeople():
    with open("人口普查",'r') as f:
        for i in f:
            # 去除空格
            if len(i) > 1:
                yield i
peo = getPeople()

all_peo = sum(eval(g)["people"] for g in peo)
# peoCount = eval(peo.__next__())
# print(peoCount["people"])

print(all_peo)
# 迭代器只能迭代一次 只能遍历一次，从新遍历需要从新获取
newP = getPeople()
for g in newP:
    a = eval(g)['people']
    pe = a/all_peo * 100
    print("百分比 %.2f %%" %pe)