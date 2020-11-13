# 说明
# read(3) 代表读取3个字符，
# 其余的文件内光标移动都是以字节为单位的，如seek，tell，read。truncate
# f.flush() : 将文件内容从内存刷到硬盘
# f.closed(): 文件如果关闭，则返回True
# f.ecoding(): 查看使用open打开文件的编码
# f.tell(): 查看文件处理当前的光标位置
# f.seek(3): 从开头算起，将光标移动到第三个字节
# f.truncate(10): 从开头算起，将文件只保留从0-10个字节的内容，文件必须以写方式打开，但是w和w+除外

# 打开文件 open 默认编码是电脑的编码
"""
# 文件打开模式 r : 可读 w ： 可写 a ： 追加
# r+:读写  w+：写读  x+：写读 a+：写读
f = open("陈粒","r",encoding="utf-8") #句柄
# data = f.read() # 读取全部
print(f.readable())  # 是否可读
print(f.readline()) # 一行一行的读
print(f.readline())
print(f.readline())
print(f.readline())
data = f.readlines()
print(data)
f.close()
"""
"""
# 文件写入
f = open("陈粒1","w")
# f.read()
f.write("111111\n")
f.write("222222\n")
f.writable() # True
f.writelines(["5555\n","34444\n"]) # 只能写字符串
f.close()

#文件追加
f = open("陈粒1","a")
f.write("写到文件最后\n")
"""
# f = open("陈粒1","r+")
# # data = f.read()
# # print(data)
# f.write("新写入哈哈哈")
# f.close()

# f = open("陈粒1","r+")
# data = f.readlines()
# print(data)
# f.close()
"""
# 文件修改
f = open("陈粒1","r+")
data = f.readlines()
f.close()
for i in data:
    print(i)
f = open("陈粒1","w")
f.writelines(data[0])
print(data[0])
f.close()
"""
# # 不需要进行close 操作
# with open("a.txt",'w') as f:
#     f.write("12345321")
# # 复制操作
# with open("陈粒1",'r') as src_f,\
#         open("a.txt",'w') as dst_f:
#     data = src_f.read()
#     dst_f.write(data)
#
# print("======================")
# f.tell() 光标位置
# f.seek(1)  设置光标位置
# f.read(4) 读取4个字符
# f.truncate(10)  截取 十个字符
# open("a.txt",'r',newline='') 读取文件中真正的转换符

"""
f = open("a.txt",'r+')
# print(f.tell())
# # print(f.readlines())
# f.readline()
# f.seek(3)
# print(f.read(4))
# print(f.tell())
f.truncate(10)

f.close()
"""

"""
b模式可以处理视频，图片等，可以跨平台，存储方式都是二进制方式，跨平台性好

open 默认打开水方式是 rb

"""
# b模式 ,不能设置 encoding 编码格式
# f = open("a.txt",'rb')
# data = f.read()
# # 字符串 ====》 encode ====》 bytes 存储过程
# print(data)
# print(data.decode("utf-8"))
# f.close()

# wb 模式
# f = open("b.txt",'wb')
# # f.write("111111111\n") # 字符串不能写入
#
# f.write(bytes("1111111111\n",encoding="utf-8"))
# f.write("232323杨建".encode("utf-8"))
# f.close()

# ab模式 追加
# f = open("b.txt",'ab')
# print(f.tell())
# # f.write("111111111\n") # 字符串不能写入
# f.write("232323杨建".encode("utf-8"))
# # f.flush() # 保存
# print(f.tell())
# f.close()

