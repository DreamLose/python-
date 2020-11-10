# 字符串掌握： join split find   strip upper lower

"""
-----------------字符串函数
"""
strS = "aLex"
# 首字母大写
s = strS.capitalize()
print(s)
# 所有字母变小写
s1 = strS.casefold()
print(s1)
s2 = strS.lower()
print(s2)
# 判断字母是否都是大写
s2 = strS.isupper()
# 所有字母变大写
s2 = strS.upper()

# 居中,设置宽度，内容居中，* 空白位置填充
print("----------居中,设置宽度，内容居中，* 空白位置填充")
s3 = strS.center(20,"*")
print(s3)
print("------------------")
#ljust 居左，设置宽度，内容居左，* 空白位置填充
s3 = strS.ljust(23,"*")
print(s3)
#rjust 居右，设置宽度，内容居右，* 空白位置填充
s3 = strS.rjust(23,"*")
print(s3)
#计算字符串中出现指定字符的次数，可以指定查找范围
# count(self, sub, start=None, end=None)
s4 = strS.count("e")
print(s4)
print("------------------")
# 字符串是否以"r"结尾
s5 = strS.endswith("r")
# 字符串是否以"r"开始
s6 = strS.startswith("a")
print(s5,s6)
print("------------------")
# 从开始往后找。找到第一个返回，找不到返回 -1
s7 = strS.find("d")
print(s7)
print("------------------")
# 查找，找不到会报错
s7 = strS.index("a")
print(s7)
print("------------------")

# format 格式化，将一个字符串中的占位符替换为指定值
testStr = "i am {name}"
print(testStr)
s8 = testStr.format(name="alex")
print(s8)

testStr1 = 'i am {0},age is {1}'
s9 = testStr1.format("alex",10)
print(s9)
print("------------------")
# format_map 格式化，传入字典 {"name":"alex"}
s10 = testStr.format_map({"name":"alex"})
print(s10)
print("------------------")
# isalnum 判断字符串中是否只包含字母跟数字
testStr = "susjaf"
s = testStr.isalnum()
print(s)
print("------------------")
# isalpha 判断字符串是否只为字母/汉字
s = testStr.isalpha()
print("------------------isalpha")
print(s)

# isdecimal 判断字符串是否只为数字 十进制的数字(常用)
print("------------------isdecimal")
s = testStr.isdecimal()
print(s)
# isdigit 判断字符串是否只为数字 ,2⃣  特殊数字也能识别
print("------------------isdigit")
s = testStr.isdigit()
print(s)

# isnumeric 字符串中只包含数字字符，则返回 True，否则返回 False
print("------------------isnumeric")
s = testStr.isnumeric()
print(s)


# expandtabs 断句，6个一组，不足六个\t会补足（可以用来制作表格）
testStr = "1234567895\t99"
s = testStr.expandtabs(6)
print(s)
print('输出格式为表格')
testStr = "userName\temail\tpasswd\nliufang\tliufang@qq.com\t123\nliufang\tliufang@qq.com\t123\nliufang\tliufang@qq.com\t123\nliufang\tliufang@qq.com\t123\n"
s = testStr.expandtabs(20)
print(s)
print('输出格式为表格----end')
# isidentifier（） 方法用于判断字符串是否是有效的 Python 标识符，可用来判断变量名是否合法
a = "21212"
v = a.isidentifier()
print(v)
print('----end')
# isprintable() 是否存在不可显示的字符
# \t 制表符
# \n 换行
testStr = "odoaofosd\nfadfsda"
v = testStr.isprintable()
print(v)
print('----end')

#isspace() 是否全部为空格
testStr = "  "
v = testStr.isspace()
print(v)
print('----end')

# title() 字符串中首字母大写
testStr = 'fdaf faf fsareiff fafre fsa fa faf!'
v = testStr.title()
s = v.istitle()
print(v)
# istitle() 字符串是否是标题，首字母全部大写为真
v = testStr.istitle()
print(v,s)
# ****************** join *************
#******** join : 将字符串中的每个元素按照指定分隔符进行拼接
test = "你是疯子还是傻子"
print(test)
# t = '  '
v = "_".join(test)
print(v)
print('----end')

# 去除左右空白/换行\n/制表符\t,指定内容会去除内容
# 用于截掉字符串左边的空格或指定字符。
test = "alex"
test.lstrip()
test.rstrip()
test.strip()
v = test.rstrip("x")
print(v)
print('----end')

# 一般 maketrans() 方法需要配合 translate() 方法一起使用
# 以下实例展示了使用 maketrans() 方法加 translate() 方法将所有元音字母转换为指定的数字，并删除指定字符：。
intab = "aeiou"
outtab = "12345"
deltab = "thw"

trantab1 = str.maketrans(intab, outtab)  # 创建字符映射转换表
trantab2 = str.maketrans(intab, outtab, deltab)  # 创建字符映射转换表，并删除指定字符

test = "this is string example....wow!!!"

print(test.translate(trantab1))
print(test.translate(trantab2))

# partition():从左边开始 按照指定字符分割。找到第一个分割
test = "testdadteafdaresfd"
v = test.partition("s")
print(v)
# rpartition():从右边开始 按照指定字符分割。找到第一个分割
v = test.rpartition("s")
print(v)
# split() :指定字符分割，可以指定分割次数，获取不到指定分割的字符"s"
v = test.split("s",2)
print(v)
print('----end')
# splitlines 指定换行符分割 splitlines(True/False) 是否保留换行符
testStr = "adfafadfs\nfadfadfas\nfadfasf"
v = testStr.splitlines()
print(v)
print('----end')

# 是否以XXXX结尾或开头
testStr.startswith("w")
testStr.endswith("dwe")
# swapcase() 大小写转换
testStr = "aLxeD"
v = testStr.swapcase()
print(v)


"""
 ----------------灰魔法（几乎所有数据类型都可以用）

"""
# 通过索引获取字符串中的某个字符，
test = "dsdsd"
print(test[3])
# 设置索引范围 0 到 3
print(test[0:4])
# 设置索引范围 0 到 倒数第二位
# 切片
print(test[0:-1])
print(len(test))
# 遍历
for item in test:
    print(item)


name = "世界是我的"
age = "1800"
info = name + age
print(info)
