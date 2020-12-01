from django.db import models


# Create your models here.

class Classes(models.Model):
    """
    班级表
    """
    title = models.CharField(max_length=32)

    teacher = models.ManyToManyField('Teachers', )  # 多对多

    def __str__(self):
        return self.title


class Teachers(models.Model):
    """
    教师表
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


"""
多对多

班级
id   title
1     3班
2     4班
3     5班

老师:
id  name
1    alex
2    老妖
3    瞎驴
4    eric

老师班级关系表

id  班级id  老师id
1     1      1
2     1      2
3     1      3
4     2      1
5     2      2


班级 获取id为1的班级
obj = Classes.objects.filter(id=1).first()
添加
添加id=2的老师
obj.m.add(2)
添加2个
obj.m.add([3,4])
删
obj.m.remove(3) 删除
obj.m.clear()   删除班级id为1的全部值
改
obj.m.set([2,3,5])  -->更新id为1的班级的老师 如果存在,则不改,不存在删除.存在其他的删除
查

列举班级id=1的所有老师
ret = obj.m.all()  -->把三张表整合到一起

整合后 ret是一个老师对象的列表  [老师1(id,name),老师2(id,name)]

"""


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    # d班级
    cs = models.ForeignKey(Classes, on_delete=models.CASCADE)  # 一对多


"""
1.类代表数据库的表
2.类的对象代指数据库中的一行数据
3.ForeignKey字段代表关联表中的一行数据
4.ManyToManyField字段自动生成第三张表,依赖关联表对第三张表间接操作
"""