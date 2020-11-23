import greenlet

def eat(name):
    print("%s eat 1" % name)
     # 第二步
    g2.switch("egon")
    print("%s eat 2" % name)
    # 第四步
    g2.switch()



def play(name):
    print("%s play 1" % name)
    # 第三步
    g1.switch()
    print("%s play 2" % name)

g1 = greenlet.greenlet(eat)
g2 = greenlet.greenlet(play)
# 第一步
g1.switch("egon")
