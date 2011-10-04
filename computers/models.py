from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

from cracken.components.models import *
from cracken.files.models import File
from cracken.programs.models import Program
from cracken.companies.models import Company

class Computer(models.Model):
    ip = models.IPAddressField(_(u"IP Address"))
    files = models.ManyToManyField(File, verbose_name=_(u"Files"), blank=True, null=True)
    programs = models.ManyToManyField(Program, verbose_name=_(u"Programs"), blank=True, null=True)

    def __unicode__(self):
        return self.ip

    class Meta:
        abstract = True
        verbose_name = _(u"Computer")
        verbose_name_plural = _(u"Computers")


class Gateway(Computer):
    processor = models.ForeignKey(Processor, verbose_name=_(u"Processor"))
    memory = models.ForeignKey(Memory, verbose_name=_(u"Memory"))
    network_card = models.ForeignKey(NetworkCard, verbose_name=_(u"Network Card"))
    owner = models.ForeignKey(User, verbose_name=_(u"Owner"))

    class Meta:
        verbose_name = _(u"Gateway")
        verbose_name_plural = _(u"Gateway")


class Server(Computer):
    owner = models.ForeignKey(Company, verbose_name=_(u"Owner"))
