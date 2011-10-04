#-*- coding: utf8 -*-
from django.db import models

class Program(models.Model):
    name = models.CharField(u"Nazwa", max_length=50)
    price = models.FloatField(u"Cena")
    port = models.IntegerField(u"Port")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Program"
        verbose_name_plural = u"Programy"
