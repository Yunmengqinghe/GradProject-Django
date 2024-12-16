from django.contrib import admin
from django.contrib.auth.hashers import make_password

from CollegeAdmin.models import CollegeAdminInfo

admin.site.site_title = '系统管理员后台'
admin.site.index_title = '信息管理模块'
admin.site.site_header = "毕设管理系统"

# Register your models here.
@admin.register(CollegeAdminInfo)
class CollegeAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'college')
    list_per_page = 20
    ordering = ('id',)

    def save_model(self, request, obj, form, change):
        if obj.password:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
