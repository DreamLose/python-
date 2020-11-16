class Room:
    tag = 1
    def __init__(self,name,owner,width,length,height):
        self.name=name
        self.owner=owner
        self.width=width
        self.length = length
        self.height=height
    @property   #
    def mianji(self):
        return self.width * self.length
    @property  #静态属性 把函数封装成属性
    def tiji(self):
        return self.width * self.length * self.height
    @classmethod  #类方法
    def tell_info(cls):
        print("这是个类方法---",cls.tag)
    @staticmethod  #类的工具包 与类无关的方法
    def wash_room(a,b):
        print("%s和%s在清洗房间" %(a,b))

    def test(x,y):  # 只有类可以调用.实例不可以
        print("%s和%s在吃房间" %(x,y))


r1 = Room('别墅','吉泽',100,100,100)
res = r1.mianji
print(res)
print("%s 住的 %s 总面积是%s:" %(r1.owner,r1.name,r1.mianji))
print(r1.tiji)
Room.tell_info()
r1.wash_room('高渐离','阿珂')
Room.wash_room("公孙离",'后裔')
Room.test('2','3')