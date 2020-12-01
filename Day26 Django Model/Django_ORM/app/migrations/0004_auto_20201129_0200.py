# Generated by Django 3.0.1 on 2020-11-29 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.Publish'),
            preserve_default=False,
        ),
    ]