#-*- coding: utf8 -*-

from django.contrib import admin

from programs.models import *


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'port')


admin.site.register(Program, ProgramAdmin)
