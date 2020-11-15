import shelve
f = shelve.open(r'shelve')  # 目的： 把一个字典放到文本里
# f['stu1_info'] = {'name':'alex','age':18}
# f['stu2_info'] = {'name':'小泽玛拉','age':25}
# f['school_info'] = {'website':'www.baidu.com','city':"hebei"}
# f.close()

print(f.get("stu1_info")['age'])