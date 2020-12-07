from django.db import models

# Create your models here.


class Direction(models.Model):
    """
    方向类
    """
    name = models.CharField(verbose_name='名称',max_length=32)
    classification = models.ManyToManyField('Classification')
    class Meta:
        db_table = 'Direction'
        verbose_name_plural = '方向(视频方向)'
    def __str__(self):
        return self.name



class Classification(models.Model):
    """
    分类类
    """
    name = models.CharField(max_length=32)
    class Meta:
        db_table = 'Classification'
        verbose_name_plural = '分类'
    def __str__(self):
        return self.name

class Level(models.Model):
    """
    水平
    """
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'Level'
        verbose_name_plural = '水平'
    def __str__(self):
        return self.name

class Video(models.Model):
    status_choice=(
        (1,'下线'),
        (2,'上线'),
    )
    status = models.IntegerField(verbose_name='状态',choices=status_choice,default=1)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    classification = models.ForeignKey('Classification',null=True,blank=True,on_delete=models.CASCADE)
    weight = models.IntegerField(verbose_name='权重(按从大到小排列)',default=0)
    title = models.CharField(verbose_name='标题',max_length=32)
    summary = models.CharField(verbose_name='简介',max_length=32)
    img = models.CharField(verbose_name='图片',max_length=32)
    href = models.CharField(verbose_name='视频地址',max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Video'
        verbose_name_plural= '视频'

    def __str__(self):
        return self.title

"""
瀑布流 表
"""
class Img(models.Model):
    src = models.FileField(max_length=32,verbose_name='图片路径',upload_to='static/img/')
    title =models.CharField(max_length=16,verbose_name='标题')
    summary = models.CharField(max_length=128,verbose_name='简介')
    class Meta:
        verbose_name_plural = '图片表'
    def __str__(self):
        return self.title