class Chinese:
    '这是一个中国的类'
     # 数据属性
    country="china"
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def eatFunc(self):
        print("%s 正在吃饭。。。。" %self.name)
    def chadui(self):
        print("%s正在插队。。。" %self.name)

p1 = Chinese('龙泽老师',43,'女')
print(p1.__dict__)

# 查看
print(p1.name)
print(p1.country)
print(p1.eatFunc)

# 增加
p1.job = "电影演员"
print(p1.__dict__)

# 修改
p1.country = "日本"

print(p1.country)

# 删除
del p1.country
print(p1.__dict__)




