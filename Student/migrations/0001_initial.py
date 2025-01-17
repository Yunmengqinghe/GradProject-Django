# Generated by Django 5.1.1 on 2024-12-10 16:01

import Student.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('College', '0001_initial'),
        ('Mentor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='学生编号')),
                ('password', models.CharField(max_length=128, verbose_name='用户密码')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('major', models.CharField(max_length=30, verbose_name='学科专业')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='College.collegeinfo', verbose_name='学院编号')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息列表',
            },
        ),
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='交流编号')),
                ('message', models.TextField(blank=True, null=True, verbose_name='信息')),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发送时间')),
                ('status', models.IntegerField(choices=[(0, '学生'), (1, '导师')], verbose_name='发送方')),
                ('is_read', models.BooleanField(default=False, verbose_name='交流状态')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='Mentor.mentorinfo', verbose_name='导师编号')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='Student.studentinfo', verbose_name='学生编号')),
            ],
            options={
                'verbose_name': '毕设交流记录',
                'verbose_name_plural': '毕设交流记录列表',
                'ordering': ['-send_date'],
            },
        ),
        migrations.CreateModel(
            name='GraduationStage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='阶段审核编号')),
                ('status', models.IntegerField(blank=True, choices=[(0, '开题报告'), (1, '中期报告'), (2, '终稿'), (3, '答辩')], null=True, verbose_name='毕设阶段')),
                ('submission_file', models.FileField(blank=True, null=True, upload_to=Student.models.user_directory_path, verbose_name='提交文件')),
                ('submission_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='提交时间')),
                ('review_date', models.DateTimeField(blank=True, null=True, verbose_name='审核时间')),
                ('review_score', models.IntegerField(blank=True, null=True, verbose_name='审核评分')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graduation_stages', to='Mentor.topicinfo', verbose_name='课题编号')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_graduation_stages', to='Student.studentinfo', verbose_name='学生编号')),
            ],
            options={
                'verbose_name': '毕设阶段成果',
                'verbose_name_plural': '毕设阶段成果列表',
            },
        ),
        migrations.CreateModel(
            name='TopicApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='选题申请编号')),
                ('student_description', models.TextField(blank=True, null=True, verbose_name='学生介绍')),
                ('application_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='申请时间')),
                ('status', models.IntegerField(choices=[(0, '待审核'), (1, '同意'), (2, '拒绝')], default=0, verbose_name='审核状态')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_applications', to='Student.studentinfo', verbose_name='学生编号')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='Mentor.topicinfo', verbose_name='课题编号')),
            ],
            options={
                'verbose_name': '选题申请信息',
                'verbose_name_plural': '选题申请列表',
            },
        ),
    ]
