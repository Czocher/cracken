from django.contrib import admin

from files.models import *


class FileAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(File, FileAdmin)
