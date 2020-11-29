from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    pub_date=models.DateField()
    # author=models.CharField(max_length=25,null=False)
    desc=models.CharField(max_length=255)

    # 多对多 -->可以手动创建
    # author = models.ManyToManyField('Author')
    # 关联出版社,默认关联主键
    publish=models.ForeignKey('Publish',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 手动创建多对多表
class Book_Author(models.Model):
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)

# 多表查询
# 出版社
# 一对多,一个出版社可以出版多本书,一本书只有一个出版社
class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

# 作者
class Author(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=20)
    def __str__(self):
        return self.name


