#-*- coding: utf8 -*-

from django.db import models

class Company(models.Model):
    name = models.CharField(u"Nazwa", max_length=100)
    quotation = models.FloatField(u"Notowanie")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Przediębiorstwo"
        verbose_name_plural = u"Przedsiębiorstwa"
