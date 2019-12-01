# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Aluser

# Register your models here.


class AluserAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Aluser, AluserAdmin)
