name = ["llala",'吉泽明步']
def changeName():
    global  name # 加上次行，修改的就是全局变量
    name = "小家"
    print(name)
def changeNameNews():
    name[0] = '龙泽'
    print(name)
changeNameNews()

print(name)

# nonlocal :上一级的变量
def ll():
    name = "我是第一级"
    def hh():
        nonlocal name
        name = "我是第二级"
    hh()
    print(name)
ll()


