# class Chinese:
#     '这是一个中国的类'
#      # 数据属性
#     country="china"
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def eatFunc(self):
#         print("%s 正在吃饭。。。。" %self.name)
#     def chadui(self):
#         print("%s正在插队。。。" %self.name)
#
# p1 = Chinese('泷泽萝拉',20,'女')
# print(p1.country)
# p1.country = "日本"
# print("类属性--->",Chinese.country)
# print("实例属性--->",p1.country)

country = "中国----"
class Chinese:
    '这是一个中国的类'
     # 数据属性
    country="china"  #这里是存在类的字典里,只能通过__dict__["country"] 或者 . 获取
    l = ['a','b']
    def __init__(self,name,age,gender):
        print("打印的是变量===",country)
        self.name = name
        self.age = age
        self.gender = gender
    def eatFunc(self):
        print("%s 正在吃饭。。。。" %self.name)
    def chadui(self):
        print("%s正在插队。。。" %self.name)


p1 = Chinese('泷泽萝拉',20,'女')
print(p1.country)
p1.country = "日本"
print("类属性--->",Chinese.country)
print("实例属性--->",p1.country)
# print(p1.l)
# p1.l = [1,2,3]
# print(p1.l)
# print(Chinese.l)

p1.l.append("c")  # 类中的也会修改
print(p1.l)
print(Chinese.l)
