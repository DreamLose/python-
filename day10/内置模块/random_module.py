import random

# r = random.random()
# r = random.randint(1,20)
r = random.randrange(10)
r = random.choice([12,23,212,4,13,32,4,31,231]) # 随机选一个
r = random.sample([12,23,212,4,13,32,4,31,231],2)  # 随机选俩个
r = random.uniform(1,4)

print(r)
l = [1,24,43,1,21,1,2]
random.shuffle(l) # 数组打乱顺序
print(l)

# 随机验证吗
def v_code():
    ret = ""
    for i in range(4):
        num = random.randint(0,9)
        alf = chr(random.randint(97,122)) #随机大写字母
        alf1 = chr(random.randint(65,90)) #随机小写字母
        res = str(random.choice([num,alf,alf1]))
        ret += res
    return ret
print(v_code())