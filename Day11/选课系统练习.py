class School:
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr



class Student:
    def __init__(self,name,school,grade):
        self.name = name
        self.school=school
        self.grade=grade

class Course:
    def __init__(self,name,price,prioed):
        self.name=name
        self.price=price
        self.prioed=prioed
class Teacher:
    def __init__(self,name,school):
        self.name=name
        self.school=school
class Grade:
    def __init__(self,course,teacher):
        self.course=course
        self.teacher=teacher

dic = {"keu":"q","ley":"d","lea":"c"}
for key in dic.items():
    print(key)
for index,key in enumerate(dic.items()):
    print(index,key)
for index,key in enumerate(dic):
    print(index,key,dic[key])