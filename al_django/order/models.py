# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Order(models.Model):
    aluser = models.ForeignKey(
        'aluser.Aluser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name="상품")
    register_date = models.DateTimeField(auto_now=True, verbose_name='등록날짜')
    quantity = models.IntegerField(verbose_name='수량')

    class Meta:
        db_table = 'albatross9_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
