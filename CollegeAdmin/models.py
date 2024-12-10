from django.db import models

# Create your models here.
# 学院管理员信息表
class CollegeAdminInfo(models.Model):
    id = models.CharField(max_length = 6, primary_key = True, verbose_name = '管理员编号')
    name = models.CharField(max_length = 30, verbose_name = '姓名')
    password = models.CharField(max_length = 128, verbose_name = '用户密码')
    college = models.ForeignKey('College.CollegeInfo', on_delete = models.CASCADE, verbose_name = '学院编号')
    title = models.CharField(max_length = 30, blank = True, null = True, verbose_name = '职称')

    class Meta:
        verbose_name = '学院管理员信息'
        verbose_name_plural = '学院管理员信息列表'


# 课题审核表
class TopicReview(models.Model):
    topic = models.ForeignKey('Mentor.TopicInfo', on_delete = models.CASCADE, related_name = 'topic_reviews',
                              verbose_name = '课题编号')
    collegeAdmin = models.ForeignKey('CollegeAdminInfo', on_delete = models.CASCADE,
                                     related_name = 'admin_topic_reviews',
                                     verbose_name = '管理员编号')
    review_date = models.DateTimeField(blank = True, null = True, verbose_name = '审核日期')
    STATUS_CHOICES = [
        (0, '待审核'),
        (1, '同意'),
        (2, '拒绝'),
    ]
    status = models.IntegerField(choices = STATUS_CHOICES, default = 0, verbose_name = '审核结果')

    class Meta:
        verbose_name = '课题审核信息'
        verbose_name_plural = '课题审核信息列表'