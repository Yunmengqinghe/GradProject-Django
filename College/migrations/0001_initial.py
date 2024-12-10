# Generated by Django 5.1.1 on 2024-12-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='学院编号')),
                ('name', models.CharField(max_length=30, verbose_name='学院名称')),
            ],
            options={
                'verbose_name': '学院信息',
                'verbose_name_plural': '学院信息列表',
            },
        ),
    ]
