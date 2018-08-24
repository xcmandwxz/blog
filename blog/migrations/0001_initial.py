# Generated by Django 2.1 on 2018-08-24 02:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Atitle', models.CharField(max_length=25)),
                ('Atime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期')),
                ('Ajian', models.CharField(max_length=90)),
                ('Aimg', models.ImageField(default='background/pic01.jpg', upload_to='background')),
                ('Atext', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=11)),
                ('upwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Atype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.UserInfo'),
        ),
    ]