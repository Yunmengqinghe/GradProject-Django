from django.db import models


# Create your models here.
# 导师信息表
class MentorInfo(models.Model):
    id = models.CharField(primary_key = True, max_length = 7, verbose_name = '导师编号')
    college = models.ForeignKey('College.CollegeInfo', on_delete = models.CASCADE, verbose_name = '学院编号')
    password = models.CharField(max_length = 128, verbose_name = '用户密码')
    name = models.CharField(max_length = 30, verbose_name = '姓名')
    title = models.CharField(max_length = 30, blank = True, null = True, verbose_name = '职称')
    research_area = models.CharField(max_length = 50, blank = True, null = True, verbose_name = '研究方向')
    description = models.TextField(blank = True, null = True, verbose_name = '教师介绍')

    class Meta:
        verbose_name = '导师信息'
        verbose_name_plural = '导师信息列表'

    def __str__(self):
        return self.name


# 课题信息表
class TopicInfo(models.Model):
    id = models.AutoField(primary_key = True, verbose_name = '课题编号')
    mentor = models.ForeignKey('MentorInfo', on_delete = models.CASCADE, related_name = 'topics',
                               verbose_name = '导师编号')
    name = models.CharField(max_length = 30, verbose_name = '课题名称')
    research_area = models.CharField(max_length = 50, verbose_name = '研究方向')
    max_len = models.IntegerField(default = 1, verbose_name = '最大人数')
    requirements = models.TextField(blank = True, null = True, verbose_name = '课题要求')

    class Meta:
        verbose_name = '课题信息'
        verbose_name_plural = '课题信息列表'

    def __str__(self):
        return self.name
