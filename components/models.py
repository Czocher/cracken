from django.utils.translation import ugettext_lazy as _
from django.db import models


class Component(models.Model):
    name = models.CharField(_(u"Name"), max_length=50)
    price = models.FloatField(_(u"Price"))

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = _(u"Component")
        verbose_name_plural = _(u"Components")


class Processor(Component):
    timing = models.IntegerField(_(u"Timing"))
    cores = models.IntegerField(_(u"Number of cores"))

    class Meta:
        verbose_name = _(u"Processor")
        verbose_name_plural = _(u"Processors")


class Memory(Component):
    size = models.IntegerField(_(u"Size"))

    class Meta:
        verbose_name = _(u"Memory")
        verbose_name_plural = _(u"Memories")


class NetworkCard(Component):
    speed = models.IntegerField(_(u"Speed"))

    class Meta:
        verbose_name = _(u"Network card")
        verbose_name_plural = _(u"Network cards")
