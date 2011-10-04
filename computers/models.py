#-*- coding: utf8 -*-

from django.contrib.auth.models import User
from django.db import models

from cracken.components.models import *
from cracken.files.models import File
from cracken.programs.models import Program
from cracken.companies.models import Company

class Computer(models.Model):
    ip = models.IPAddressField(u"Adres IP")
    files = models.ManyToManyField(File, verbose_name=u"Pliki", blank=True, null=True)
    programs = models.ManyToManyField(Program, verbose_name=u"Programy", blank=True, null=True)

    def __unicode__(self):
        return self.ip

    class Meta:
        abstract = True
        verbose_name = u"Komputer"
        verbose_name_plural = u"Komputery"


class Gateway(Computer):
    processor = models.ForeignKey(Processor, verbose_name=u"Procesor")
    memory = models.ForeignKey(Memory, verbose_name=u"Pamięć")
    network_card = models.ForeignKey(NetworkCard, verbose_name=u"Karta sieciowa")
    owner = models.ForeignKey(User, verbose_name=u"Właściciel")

    class Meta:
        verbose_name = u"Brama"
        verbose_name_plural = u"Bramy"


class Server(Computer):
    owner = models.ForeignKey(Company, verbose_name=u"Właściciel")
