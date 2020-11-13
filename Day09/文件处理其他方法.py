# seek 三种模式
# 1。seek(10)
# 2.seek(10,1)
# 3.seek(10,2)  //倒叙模式
"""
f = open('a.txt','rb')
print(f.tell())
f.seek(10)
print(f.tell())
f.seek(3,1)  #相对与上次光标的位置移动光标，不能相对于0
print(f.tell())
f.close()
"""
# f = open('a.txt','rb')
# print(f.tell())
# f.seek(-5,2)
# print(f.read())
# print(f.tell())
# # f.seek(3,1)  #相对与上次光标的位置移动光标，不能相对于0
# # print(f.tell())
# f.close()

# seek 读取文件最后一行
f = open("a.txt",'rb')
# 循环文件推荐方式
# for i in f:
#     print(i)
for i in f:
    offs = -1 # 定义偏移量
    while True:
        f.seek(offs,2)
        data = f.readlines()
        print("data==%s" %data,len(data))
        if len(data) > 1:
            print("文件的最后一行是：%s" %(data[-1].decode("utf-8")))
            break
        offs*=2

f.close()
