# 字典 keys() values() items() get() update()
dict
info = {"k1":"v1","k2":"v2"}
print(info)
info.keys()
info.values()
del info["k1"]
print(info)
# 获取key，value
for k,y in info.items():
    print(k,y)
#根据序列创建字典，指定统一值
v = dict.fromkeys(['ke','323','999'],[123,"ewe"])
print(v)
# 根据key 获取值，key不存在时可以指定默认值
s = v.get("ke",23232)
print(s)
# 删除并获取值,没有对应的key返回默认值
s = v.pop("ke3",90)
print(s)

# 设置值，已经存在，不设置并获取当前key对应的值，不存在key则添加对应值并获取
v.setdefault("ke",1212)
print(v)
v.update({'ke':"232323","kk":32323})
print(v)
v.update(ke=1212,k3=33223,kk=323)
print(v)

