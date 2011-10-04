#-*- coding: utf8 -*-

from django.db import models

class File(models.Model):
    path = models.CharField(u"Ścieżka", max_length=255, unique=True)
    content = models.TextField(u"Zawartość")
    binary = models.BooleanField(u"Binarny", default=False)

    def name(self):
        return path.split('/')[-1]

    def __unicode__(self):
        return self.name(self)

    class Meta:
        verbose_name = u"Plik"
        verbose_name_plural = u"Pliki"
