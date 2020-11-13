"""
====================== 内置函数 =================
"""
print(all([1,2,3,"fda",0])) # 判断每个元素是否为真
print(all(""))  # True
print(abs(-1)) # 求绝对值
name = "alexs"
# hash : 可用来判断下载文件是否安全
print(hash(name))
print(hash(name))
print(hash(name))
# zip 拉链效果 max min
p = {"name":"吉泽明步","age": 29,"job": "teacher"}
print(list(zip(p.keys(),p.values())))
age_dic = {"alex_age":19,"吉泽明步":30,"泷泽萝拉":33}
print(max(zip(age_dic.values(),age_dic.keys())))
p = [{"name":"吉泽明步","age": 29,"job": "teacher"},
     {"name":"仓央嘉措","age": 50,"job": "teacher"},
     {"name":"小泽","age": 25,"job": "teacher"},
     {"name":"小龙","age": 40,"job": "teacher"},
     {"name":"小仓","age": 35,"job": "teacher"},]
print(max(p,key=lambda x:x["age"]))
print(chr(97))
print(ord("a"))

print(pow(3,4)) # 3**3
print(pow(3,4,2)) # 3**3%2
# 反转
l = [1,2,3,4,5]
print(list(reversed(l)))
print(l)
l = "hello"
s = slice(3,5) #切片，可以设置步长
print(l[s])
# sorted() 排序
p = [{"name":"吉泽明步","age": 29,"job": "teacher"},
     {"name":"仓央嘉措","age": 50,"job": "teacher"},
     {"name":"小泽","age": 25,"job": "teacher"},
     {"name":"小龙","age": 40,"job": "teacher"},
     {"name":"小仓","age": 35,"job": "teacher"},]
print(sorted(p,key=lambda dic:dic["age"]))

# import 不能导入字符串。__improt__ 可以导入字符串格式
import main
__import__("main")