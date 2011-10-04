#-*- coding: utf8 -*-

from django.contrib import admin

from companies.models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'quotation')


admin.site.register(Company, CompanyAdmin)
