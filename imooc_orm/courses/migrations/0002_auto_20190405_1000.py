# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-05 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('title', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False, verbose_name='课程名')),
                ('type', models.CharField(choices=[(1, '实战课'), (2, '免费课'), (0, '其它')], default=0, max_length=1, verbose_name='课程类型')),
                ('price', models.PositiveSmallIntegerField(verbose_name='价格')),
                ('volume', models.BigIntegerField(verbose_name='销量')),
                ('online', models.DateField(verbose_name='上线时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '课程信息表',
                'verbose_name_plural': '课程信息表',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('nickname', models.CharField(db_index=True, max_length=30, primary_key=True, serialize=False, verbose_name='昵称')),
                ('age', models.PositiveSmallIntegerField(verbose_name='年龄')),
                ('gender', models.CharField(choices=[(1, '男'), (2, '女'), (0, '保密')], default=0, max_length=1, verbose_name='性别')),
                ('study_time', models.PositiveIntegerField(default='0', verbose_name='学习时长(h)')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '学生信息表',
                'verbose_name_plural': '学生信息表',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('nickname', models.CharField(db_index=True, max_length=30, primary_key=True, serialize=False, verbose_name='昵称')),
                ('introduction', models.TextField(default='木有签名还！', verbose_name='简介')),
                ('fans', models.PositiveIntegerField(default='0', verbose_name='粉丝数')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '讲师信息表',
                'verbose_name_plural': '讲师信息表',
            },
        ),
        migrations.CreateModel(
            name='TeacherAssistant',
            fields=[
                ('nickname', models.CharField(db_index=True, max_length=30, primary_key=True, serialize=False, verbose_name='昵称')),
                ('hobby', models.CharField(max_length=100, null=True, verbose_name='爱好')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '助教信息表',
                'verbose_name_plural': '助教信息表',
                'db_table': 'course_assistant',
            },
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='说明'),
        ),
    ]
