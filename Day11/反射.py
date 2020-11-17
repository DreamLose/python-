class BlackMedium:
    feture='Ugly'
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
    def sell_hourse(self):
        print("[%s] 正在卖房子" %(self.name))

    def rent_hourse(self):
        print("[%s] 正组房子" % (self.name))
b1 = BlackMedium('万成置地','天露园')
# b1对象中是否有 addr1 属性
res = hasattr(b1,'addr1')
print(res)
res = hasattr(b1,'feture')
print(res)

res = getattr(b1,'name')
print(res)
res = getattr(b1,'sell_hourse')
print(res)
res()
# 没有找到会报错
# res = getattr(b1,'sell_hourseqwqw')
# print(res)
# 设置默认值,不会报错
res = getattr(b1,'sell_hourseqwqw',"没有这个属性")
print("====",res)
# 修改/新增属性
b1.ss = False
setattr(b1,'sb',True)
print(b1.sb)
setattr(b1,'name',"ll")
print(b1.__dict__)
print(b1.name)
# T添加函数属性
setattr(b1,'func',lambda x:x+1)
print(b1.__dict__)
print(b1.func(2))
# 删除属性
del b1.sb
print(b1.__dict__)
delattr(b1,"ss")
print(b1.__dict__)


print(hasattr(BlackMedium,'name'))
print(hasattr(BlackMedium,'feture'))