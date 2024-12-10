from django.db import models

# Create your models here.
# 学院信息表
class CollegeInfo(models.Model):
    id = models.AutoField(primary_key = True, verbose_name = '学院编号')
    name = models.CharField(max_length = 30, verbose_name = '学院名称')

    class Meta:
        verbose_name = '学院信息'
        verbose_name_plural = '学院信息列表'

    def __str__(self):
        return self.name