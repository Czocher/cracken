#-*- coding: utf8 -*-

from components.models import *
from django.contrib import admin


class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'timing', 'cores')


class MemoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'amount')


class NetworkCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'speed')


admin.site.register(Processor, ProcessorAdmin)
admin.site.register(Memory, MemoryAdmin)
admin.site.register(NetworkCard, NetworkCardAdmin)
