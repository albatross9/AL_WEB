# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Aluser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name="비번")
    register_date = models.DateTimeField(auto_now=True, verbose_name="등록일")

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'albatross9_aluser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자들'
