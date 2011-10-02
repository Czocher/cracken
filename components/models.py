#-*- coding: utf8 -*-

from django.db import models

class Component(models.Model):
    name = models.CharField(u"Nazwa", max_length=50)
    price = models.FloatField(u"Cena")

    class Meta:
        abstract = True
        verbose_name = u"Komponent"
        verbose_name_plural = u"Komponenty"


class Processor(Component):
    timing = models.IntegerField(u"Taktowanie")

    class Meta:
        verbose_name = u"Procesor"
        verbose_name_plural = u"Procesory"


class Memory(Component):
    amount = models.IntegerField(u"Ilość Megabajtów")

    class Meta:
        verbose_name = u"Pamięć"
        verbose_name_plural = u"Pamięci"


class NetworkCard(Component):
    speed = models.IntegerField(u"Szybkość")

    class Meta:
        verbose_name = u"Karta sieciowa"
        verbose_name_plural = u"Karty sieciowe"
