from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=32)
    price=models.FloatField()
    pub_data=models.DateField()


    authors=models.ManyToManyField('Author')
    publish=models.ForeignKey('Publish',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 作者
class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    def __str__(self):
        return self.name
# 出版社
class Publish(models.Model):
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)
    def __str__(self):
        self.name
