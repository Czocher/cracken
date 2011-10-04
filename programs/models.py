from django.utils.translation import ugettext_lazy as _
from django.db import models


class Program(models.Model):
    name = models.CharField(_(u"Name"), max_length=50)
    price = models.FloatField(_(u"Price"))
    port = models.IntegerField(_(u"Port"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u"Program")
        verbose_name_plural = _(u"Programs")
