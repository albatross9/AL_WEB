# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-01 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\uc0c1\ud488\uba85')),
                ('price', models.IntegerField(verbose_name='\uc0c1\ud488\uac00\uaca9')),
                ('description', models.TextField(verbose_name='\uc0c1\ud488\uc124\uba85')),
                ('stuck', models.IntegerField(verbose_name='\uc7ac\uace0')),
                ('register_date', models.DateTimeField(auto_now=True, verbose_name='\ub4f1\ub85d\ub0a0\uc9dc')),
            ],
            options={
                'db_table': 'albatross9_product',
                'verbose_name': '\uc0c1\ud488',
                'verbose_name_plural': '\uc0c1\ud488\ub4e4',
            },
        ),
    ]
