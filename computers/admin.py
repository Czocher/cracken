#-*- coding: utf8 -*-

from django.contrib import admin

from computers.models import *


class GatewayAdmin(admin.ModelAdmin):
    list_display = ('ip', 'owner')


class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip', 'owner')


admin.site.register(Gateway, GatewayAdmin)
admin.site.register(Server, ServerAdmin)
