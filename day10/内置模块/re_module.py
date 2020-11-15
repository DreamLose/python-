# 正则表达式
# s = "helelallaladllalexldjfdsfa"
# res = s.find("alex")
# print(res)
# res = s.partition('alex')
# print(res)
import re
# 普通字符： 大多数字符和字母都会和自身匹配
# res = re.findall("alex","ydnafndafaalexdafalaesxe")
# print(res)
# 元字符：. ^ $ * + ? {} [] | () \

# . : 通配符
# res = re.findall("a...x","dafdsawfaalerxfadfaa")
# print(res)
# res = re.findall("a..x","dafdsawfaalerxfadfaa")
# print(res)

# ^ : 只能以字符串的开头匹配 "^a..x" 匹配的字符串必须以"a" 开头，
# res = re.findall("^a..x","adaxfdsawfaalerxfadfaa")
# print(res)
# res = re.findall("^a..x","nadaxfdsawfaalerxfadfaa")
# print(res)

# $ : 只能从字符串的结尾匹配 "a..x$" 匹配的字符串必须以"x" 结尾，后四位是a..x，
# res = re.findall("a..x$","adaxfdsawfaalerxfadfaax")
# print(res)
# res = re.findall("a..x$","nadaxfdsawfaalerxfadax")
# print(res)

# 重复符号
# * : 匹配的是0 到无穷次 有几个匹配几次（贪婪匹配）
res = re.findall("d*","sddafaadddafadsdd")
print(res)
# + :  匹配的是1 到无穷次 有几个匹配几次（贪婪匹配）
res = re.findall("alex+","aksdkakdfalexxxxx")
print(res)
res = re.findall("alex*","aksdkakdfalexxxxx")
print(res)
res = re.findall("alex*","aksdkakdfale")
print(res)

# ?：匹配的是 0 到 1 次
res = re.findall("alex?","aksdkakdfale")
print(res)
res = re.findall("alex?","aksdkakdfalexxxxx")
print(res)

# {} : 万能的 ，匹配次数自己定 {0,} ==> * ; {1,} ==> + ;{0,1} ==> ? ; 其他;
res = re.findall("alex{6}","aksdkakdfalexxxxx")  # 匹配连续6个x
print(res)
res = re.findall("alex{0,1}","aksdkakdfalexxxxx") # 匹配0或者1个x，按最多匹配
print(res)

# 前面的* + ? 等都是贪婪匹配，也就是尽可能匹配(按最多匹配)，后面加?号时期变成惰性匹配(按范围最小匹配)
res = re.findall("alex+?","aksdkakdfalexxxxx")  # 只会匹配一个x
print(res)

# 元字符之 字符集 [] 只有4个特殊符号 - ^ \
# "-":范围;
res = re.findall("x[yz]","xyypuuxzpssys")  #
print(res)
res = re.findall("q[a*z]","qsafzwfaqaaq*")  #
print(res)
# 字符集 [] 只有4个特殊符号  "-":范围; d[a-z]  匹配到d后面带的任意一个字母
res = re.findall("d[a-z]",'fafsdafwf1212sfdsaf234241231')
print(res)
res = re.findall("d[a-z]*",'fafsdafwf1212sfdsaf234241231')
print(res)
# 字符集 [] 中  "^":非;
res = re.findall("d[a-z]",'fafsdafwf1212sfdsaf234241231')
print(res)
#  d[^a-z]* 匹配到d 或者d后面带的不是字母
res = re.findall("d[^a-z]*",'d21fafsdafwf1212sfdsaf234241231')
print(res)
#  "^":非;
s = "12+(34*6+2-5*(2-1))" # 首先匹配(2-1)
res = re.findall("\([^()]*\)","12+(34*6+2-5*(2-1))")
print(res)
# 元字符 之转义字符
"""
\ : 反斜杠后边跟元字符 去除特殊功能 比如  \.
    反斜杠后边跟普通字符实现特殊功能 比如  \d    
    \d ：匹配任何十进制数，相当于类[0-9]
    \D ：匹配任何非数字字符，相当于类[^0-9]
    \s ：匹配任何空白字符，相当于类[\+\n\r\f\v]
    \S ：匹配任何非空白字符，相当于类[^\+\n\r\f\v]
    \w ：匹配任何字母数字字符，相当于类[a-zA-Z0-9_]
    \W ：匹配任何非字母数字字符，相当于类[^a-zA-Z0-9_]
    \b ：匹配一个特殊字符边界，比如空格，&，# 等
"""
res = re.findall("\d+","12+(34*6+2-5*(2-1))")
print(res)
res = re.findall("[0-9]+","12+(34*6+2-5*(2-1))")
print(res)
res = re.findall("\D+","12+(34*6+2-5*(2-1))")
print(res)
res = re.findall("[^0-9]+","12+(34*6+2-5*(2-1))")
print(res)

res = re.findall("\S+","hello world")
print(res)
res = re.findall("\s+","hello world")
print(res)
print("================")

res = re.findall("\w+","hello world_1312")
print(res)
res = re.findall("\W+","hello world_dw121")
print(res) # 只会匹配空格

res = re.findall("I\b","I am lIst")
print(res)
# r ：原生字符串，r后的字符串不做任何转义
res = re.findall(r"I\b","I am lIst")
print(res)
#\b 本身在python中是有意义的  需要转义
res = re.findall("I\\b","hello I am lIst")
print(res)

#| :  ka|b 匹配ka 或者 b
res = re.findall(r"ka|b","fafnafeb")
print(res)
res = re.findall(r"ka|b","dkabafnafeka|bkb")
print(res)

#  + :分组
res = re.findall("(abc)+","abcccc")
print(res)
# 优先取组里的abc
res = re.findall("(abc)+","abcabc")
print(res)
# 取消优先级
res = re.findall("(?:abc)+","abcabc")
print("======",res)
# (?P<>) :固定写法

# search 只会找一个 返回的是一个对象


res = re.search("(?P<name>[a-z]+)\d+","alex12xiaocang34")
print(res.group())
print(res.group("name"))

res = re.search("(?P<name>[a-z]+)(?P<age>\d+)","alex12xiaocang34")
print(res.group())
print(res.group("age"))
# 12+(34*6+2-5*(2-1)+(4*4+4)) ：首先匹配前面一个括号
res = re.search("\([^()]+\)","12+(34*6+2-5*(2-1)+(4*4+4))")
print(res.group())
print('==========')
# re 模块下常用方法
# match 只会从字符串开始匹配
res = re.match("\d+","alex34dafs34")
print(res)
res = re.match("\d+","21alex34dafs34")
print(res.group())
#  split 分割
res = re.split(" ",'hello abc def')
print(res)
# 以空格 和 ｜ 分割
res = re.split("[ ｜]",'hello abc｜def')
print(res)
# 按a或者b分割，左右分开，没有的元素显示为 空
res = re.split("[ab]",'asdabcd')
print(res)

# sub ：替换
#把数字替换成A
res = re.sub("\d+","A","dwfwf121werw12")
print(res)
#把数字替换成A,限定次数
res = re.sub("\d+","A","dwfwf121werw12",1)
print(res)
print("++++++++++")
# subn: 返回替换后的字符串和替换的次数
res = re.subn("\d+","A","dwfwf121werw12")
print(res)

# compile 编译, 提前写好规则
com = re.compile("\d+")
res = com.findall("dsaf1212sas")
print(res)

# finditer 返回的迭代器 （同 findall()）
res = re.finditer('\d+','ewr212dsew312')
print(res)
print(next(res).group())
print(next(res).group())

# 分组 默认会把组里匹配的内容返回
res = re.findall("www\.(baidu|163)\.com",'www.baidu.com')
print(res)
# "?:"  去掉分组的优先级
res = re.findall("www\.(?:baidu|163)\.com",'www.baidu.com')
print(res)