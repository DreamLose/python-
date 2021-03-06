# Generated by Django 3.1.3 on 2020-12-07 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '分类',
                'db_table': 'Classification',
            },
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=16)),
                ('summary', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '水平',
                'db_table': 'Level',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, '下线'), (2, '上线')], default=1, verbose_name='状态')),
                ('weight', models.IntegerField(default=0, verbose_name='权重(按从大到小排列)')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('summary', models.CharField(max_length=32, verbose_name='简介')),
                ('img', models.CharField(max_length=32, verbose_name='图片')),
                ('href', models.CharField(max_length=32, verbose_name='视频地址')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.classification')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.level')),
            ],
            options={
                'verbose_name_plural': '视频',
                'db_table': 'Video',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('classification', models.ManyToManyField(to='app01.Classification')),
            ],
            options={
                'verbose_name_plural': '方向(视频方向)',
                'db_table': 'Direction',
            },
        ),
    ]
