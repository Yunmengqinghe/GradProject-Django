# Generated by Django 5.1.1 on 2024-12-17 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CollegeAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicreview',
            name='collegeAdmin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_topic_reviews', to='CollegeAdmin.collegeadmininfo', verbose_name='管理员编号'),
        ),
    ]
