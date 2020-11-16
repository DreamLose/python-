# class Hand:
#     pass
# class Foot:
#     pass
# class Trunk:
#     pass
# class Head:
#     pass
#
#
#
#
# class Person:
#     def __init__(self,id_num,name):
#         self.id_num = id_num
#         self.name = name
#         self.hand = Hand()
#         self.foot = Foot()
#         self.trunk = Trunk()
#         self.head = Head()
#
# p1 = Person('121212','晓得')
# print(p1.__dict__)



class School:
    def __init__(self,name,addr):
        self.name = name  #学校名称
        self.addr = addr #学校地址
    def zhaosheng(self):
        print("%s正在招生" %(self.name))

class Course:
    def __init__(self,name,price,period,school):
        self.name = name   #课程名称
        self.price = price #课程价格
        self.period = period #课程周期
        self.school = school #课程所属学校

class Teacher:
    def __init__(self,name,school,course):
        self.name = name  # 老师名称
        self.school = school  # 老师所属学校
        self.course = course  #课程

s1 = School('千锋','北京')
s2 = School('千锋','南京')

c1 = Course('Linux',10,'1h',s1)

# print(c1.school.name)
msg = """
   1 前锋 北京校区
   2 前锋 南京校区
   """
while True:
    print(msg)
    choice = input("用户选择:")
    meum = {
        '1':s1,
        '2':s2,
    }
    school_obj = meum[choice]
    name = input("课程名称:")
    price = input('课程价格:')
    peroid = input('课程周期:')
    cr = Course(name,price,peroid,school_obj)
    print('[%s] 课程属于[%s]校区' %(cr.name,cr.school.name))


