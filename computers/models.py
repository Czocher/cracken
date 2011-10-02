#-*- coding: utf8 -*-

from django.db import models
from cracken.components.models import *
from cracken.files.models import File
from cracken.servers.models import Server

class Computer(models.Model):
    ip = models.IPAddressField(u"Adres IP")
    files = models.ManyToManyField(File, verbose_name=u"Pliki")
    servers = models.ManyToManyField(Server, verbose_name=u"Serwery")

    class Meta:
        abstract = True
        verbose_name = u"Komputer"
        verbose_name_plural = u"Komputery"


class Gateway(Computer):
    processor = models.ForeignKey(Processor, verbose_name=u"Procesor")
    memory = models.ForeignKey(Memory, verbose_name=u"Pamięć")
    network_card = models.ForeignKey(NetworkCard, verbose_name=u"Karta sieciowa")

    class Meta:
        verbose_name = u"Brama"
        verbose_name_plural = u"Bramy"
