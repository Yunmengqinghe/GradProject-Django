from django.contrib import admin
from django.contrib.auth.hashers import make_password

from Mentor.models import MentorInfo


# Register your models here.
@admin.register(MentorInfo)
class MentorInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'college')
    list_per_page = 20
    ordering = ('id',)

    def save_model(self, request, obj, form, change):
        # 如果密码字段不为空，则加密它
        if obj.password:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
