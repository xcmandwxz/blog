from django.contrib import admin
from .models import *
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','uname','upwd']


class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id','Atitle','Atime','Ajian','Atext']


admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(Article,ArticleAdmin)