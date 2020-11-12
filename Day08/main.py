# li = [1,2,3,4,5,6,7,8]
#
# countNum = 0
# for item in range(1,9):
#     for item2 in range(1,9):
#         if item != item2:
#             newStr = str(item)+str(item2)
#             print(newStr)
#             countNum += 1
# print("-----------count:",countNum)
#
# for v in range(1,10):
#     for i in range(1,v+1):
#         sumNu = v * i
#         print(str(v) + "*" + str(i) + "=" + str(sumNu) + "\t",end="")
#     print("")


# 公鸡 5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买100只鸡，公鸡，母鸡，小鸡各多少只
# 100文钱 最多可以买20 只公鸡，30只母鸡，
#  x    y      z
# 公鸡 5 母鸡 3 小鸡 3--1
# 100 --100只
# 5 * x + 3 * y + z / 3 =100
# x + y + z = 100
"""
for num in range(1,101):
    x = int(num)
    y = (100 - 7 * x)/4
    z = (3 * x + 300) / 4
    if y < 0 or z < 0:
        continue
    if y - int(y) > 0 and z - int(z) > 0:
        pass
    else:
        print(x,y,z)
# 推荐方法

for x in range(1,100//5):
    for y in range(1,100//3):
        for z in range(1,101):
            if x + y + z == 100 and 5*x + 3*y + z/3 == 100:
                print(x,y,z)
"""

# li = ['daf','fadsf','fs']
# a = "_".join(li)
# print(a)
li = []
for i in range(1,301):
    strS = "alex-" + str(i) + "\talex" + str(i) + "@live.com\t" + "pwd"+str(i) + "\n"
    li.append(strS)
# print(li)
# for i in li:
#     print(i.expandtabs(15))

while True:
    nu = input("请输入查看的页码：")
    nu = int(nu)
    start = (nu -1) * 10
    end = nu * 10
    for i in li[start : end]:
        print(i.expandtabs(15))
str