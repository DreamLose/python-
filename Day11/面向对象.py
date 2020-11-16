


# name = "小仓"
# gender = "male"
# type = "拉布拉多"

# dog1 的特征
dog1 = {'name':"小仓",
        'gender':"male",
        'type':"拉布拉多"}
dog2 = {'name':"alex",
        'gender':"male",
        'type':"拉布拉多"}
def dogJiao(dog):
    print("[%s]狗在叫。。" %dog['name'])
def dogEat(dog):
    print("[%s]狗在吃饭。。" %dog['name'])

dogJiao(dog1)
dogEat(dog2)


def dog(name,gender,type):
    def dogJiao(dog):
        print("[%s]狗在叫。。" % dog['name'])

    def dogEat(dog):
        print("[%s]狗在吃饭。。" % dog['name'])
    # def init():
    dog = {'name': name,
            'gender': gender,
            'type': type,
           'jiao':dogJiao,
           'eat':dogEat
            }
    return dog

d = dog('小白','male','京巴')

d['jiao'](d)
