#-*- coding: utf8 -*-
from django.db import models

class Server(models.Model):
    name = models.CharField(u"Nazwa", max_length=50)
    price = models.FloatField(u"Cena")
    port = models.IntegerField(u"Port")

    class Meta:
        verbose_name = u"Serwer"
        verbose_name_plural = u"Serwery"
