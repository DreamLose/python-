class Vehicle:
    Country = "China"
    def __init__(self,name,speed,load,power):
        self.name=name
        self.speed=speed
        self.load=load
        self.power=power
    def run(self):
        print("启动了")

class Subway(Vehicle):
    def __init__(self,name,speed,load,power,line):
        # Vehicle.__init__(self,name,speed,load,power)
        super().__init__(name,speed,load,power)
        self.line = line
    def show(self):
        print(self.name,self.line)
    def run(self):
        # Vehicle.run(self)
        super().run()
        print("%s %s 开动了" %(self.name,self.line))
line13 = Subway('北京地铁','100km/h',10000,'电','13号线')
line13.show()
line13.run()
#
print(line13.__class__)


# 优化后
# class Vehicle:
#     Country = "China"
#     def __init__(self,name,speed,load,power):
#         self.name=name
#         self.speed=speed
#         self.load=load
#         self.power=power
#     def run(self):
#         print("启动了")
#
# class Subway(Vehicle):
#     def __init__(self,name,speed,load,power,line):
#         super.__init__(self,name,speed,load,power)
#         self.line = line
#     def show(self):
#         print(self.name,self.line)
#     def run(self):
#         Vehicle.run(self)
#         print("%s %s 开动了" %(self.name,self.line))
# line13 = Subway('北京地铁','100km/h',10000,'电','13号线')
# line13.show()
# line13.run()