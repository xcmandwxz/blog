from django.db import models
import django.utils.timezone as timezone


class UserInfo(models.Model):
    uname = models.CharField(max_length=11)
    upwd = models.CharField(max_length=20)



class Article(models.Model):
    Atitle = models.CharField(max_length=25)
    Atime = models.DateTimeField('发布日期',default=timezone.now)
    Ajian = models.CharField(max_length=90)
    Aimg = models.ImageField(upload_to='background',default="/static/background/pic01.jpg")
    Atext = models.TextField(blank=True,null=True)
    Atype = models.ForeignKey(UserInfo,on_delete=models.CASCADE,default=1)
