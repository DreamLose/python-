#循环 求1-100内所有数的和 4950
startNum = 1
sumNum = 0
while startNum < 101:
    sumNum = sumNum + startNum
    startNum = startNum + 1
print ("和：")
print (sumNum)
print ("------------end-----------")
#输出1，2，3，4，5，6，8，9，10
startNum = 1
while startNum < 11:
    if startNum != 7:
        print (startNum)
    startNum = startNum + 1
print ("------------end-----------")
"""
#输出1-100内的所有奇数
startNum = 1
while startNum < 100:
    if startNum % 2 ==1 :
        print ("奇数为：",startNum)
    else:
        print ("偶数为：",startNum)
    startNum = startNum + 1
    print ("------------end-----------")
"""

#输出1-2+3-4+5。。。。的和 50
startNum = 1
sumNum = 0
while startNum < 100:
    if startNum % 2 ==1 :
       sumNum = startNum + sumNum
    else:
        sumNum = sumNum - startNum
    startNum = startNum + 1

print ("合为：",sumNum)
print ("------------end-----------")

loginCount = 0
loginName = "root"
loginPass = "root"
while loginCount < 3:
    name = input("输入姓名：")
    passw = input("输入密码：")
    if name == loginName and passw == loginPass:
        print ("登陆成功")
        break
    else:
        print ("登陆失败，请重新登陆。。。")
    loginCount = loginCount + 1
if loginCount > 3:
    print ("3次机会失败，无法登陆")
print ("------------end-----------")


