from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    pub_date=models.DateField()
    author=models.CharField(max_length=25,null=False)
    desc=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Author(models.Model):
    name=models.CharField(max_length=20)

