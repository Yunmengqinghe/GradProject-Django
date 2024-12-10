import os

from django.db import models
from django.utils import timezone


# Create your models here.
class StudentInfo(models.Model):
    id = models.CharField(primary_key = True, max_length = 8, verbose_name = '学生编号')
    college = models.ForeignKey('College.CollegeInfo', on_delete = models.CASCADE, verbose_name = '学院编号')
    password = models.CharField(max_length = 128, verbose_name = '用户密码')
    name = models.CharField(max_length = 30, verbose_name = '姓名')
    major = models.CharField(max_length = 30, verbose_name = '学科专业')

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息列表'


# 选题申请表
class TopicApplication(models.Model):
    id = models.AutoField(primary_key = True, verbose_name = '选题申请编号')
    topic = models.ForeignKey('Mentor.TopicInfo', on_delete = models.CASCADE, related_name = 'applications',
                              verbose_name = '课题编号')
    student = models.ForeignKey('StudentInfo', on_delete = models.CASCADE, related_name = 'student_applications',
                                verbose_name = '学生编号')
    student_description = models.TextField(blank = True, null = True, verbose_name = '学生介绍')
    application_date = models.DateTimeField(default = timezone.now, verbose_name = '申请时间')
    STATUS_CHOICES = [
        (0, '待审核'),
        (1, '同意'),
        (2, '拒绝'),
    ]
    status = models.IntegerField(choices = STATUS_CHOICES, default = 0, verbose_name = '审核状态')

    class Meta:
        verbose_name = '选题申请信息'
        verbose_name_plural = '选题申请列表'


def user_directory_path(instance, filename):
    student_id = instance.student.id
    return os.path.join('users', student_id, filename)


# 毕设阶段成果表
class GraduationStage(models.Model):
    id = models.AutoField(primary_key = True, verbose_name = '阶段审核编号')
    topic = models.ForeignKey('Mentor.TopicInfo', on_delete = models.CASCADE, related_name = 'graduation_stages',
                              verbose_name = '课题编号')
    student = models.ForeignKey('StudentInfo', on_delete = models.CASCADE, related_name = 'topic_graduation_stages',
                                verbose_name = '学生编号')
    STAGE_STATUS_CHOICES = [
        (0, '开题报告'),
        (1, '中期报告'),
        (2, '终稿'),
        (3, '答辩')
    ]
    status = models.IntegerField(choices = STAGE_STATUS_CHOICES, blank = True, null = True,
                                 verbose_name = '毕设阶段')
    submission_file = models.FileField(upload_to = user_directory_path, blank = True, null = True,
                                       verbose_name = '提交文件')
    submission_date = models.DateTimeField(default = timezone.now, blank = True, null = True, verbose_name = '提交时间')
    review_date = models.DateTimeField(blank = True, null = True, verbose_name = '审核时间')
    review_score = models.IntegerField(blank = True, null = True, verbose_name = '审核评分')

    class Meta:
        verbose_name = '毕设阶段成果'
        verbose_name_plural = '毕设阶段成果列表'


# 毕设交流记录表
class MessageInfo(models.Model):
    id = models.AutoField(primary_key = True, verbose_name = '交流编号')
    student = models.ForeignKey('StudentInfo', on_delete = models.CASCADE, related_name = 'sent_messages',
                                verbose_name = '学生编号')
    mentor = models.ForeignKey('Mentor.MentorInfo', on_delete = models.CASCADE, related_name = 'received_messages',
                               verbose_name = '导师编号')
    message = models.TextField(blank = True, null = True, verbose_name = '信息')
    send_date = models.DateTimeField(default = timezone.now, verbose_name = '发送时间')
    STATUS_CHOICES = [
        (0, '学生'),
        (1, '导师')
    ]
    status = models.IntegerField(choices = STATUS_CHOICES, verbose_name = '发送方')
    is_read = models.BooleanField(default = False, verbose_name = '交流状态')

    class Meta:
        verbose_name = '毕设交流记录'
        verbose_name_plural = '毕设交流记录列表'
        ordering = ['-send_date']
