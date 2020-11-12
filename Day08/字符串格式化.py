msg = 'i am %s my hobby is alal' %"lhf"
print(msg)
msg = 'i am %s my hobby is %s' %("lhf","dsd")
print(msg)
# %d 只能接受数字; %s 接受所有; %f 接受浮点数默认保留6位 %.2f 保留2位小数
msg = 'i am %s my hobby is %s' %("lhf","dsd")

# 打印百分比
tap1 = "percent %.2f%%" % 12.9921212
print(tap1)
tp = "i am %(name)s age %(age)d" % {"name":"alex","age":12}
print(tp)


# format 格式化
tp1 = "i am {},age {},{}".format("seten",18,"alex")
print(tp1)
tp1 = "i am {2},age {1},{0}".format("seten",18,"alex")
print(tp1)
tp1 = "i am {2},age {1},{0}".format("seten",18,"alex")
tp1 = "i am {2},age {2},{2}".format("seten",18,"alex")
print(tp1)
tp1 = "i am {name},age {age},{name}".format(name="seten",age=18)
print(tp1)
tp1 = "i am {name},age {age},{name}".format(**{"name":"seten","age":18})
print(tp1)