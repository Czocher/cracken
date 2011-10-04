from django.utils.translation import ugettext_lazy as _
from django.db import models

class Company(models.Model):
    name = models.CharField(_(u"Name"), max_length=100)
    quotation = models.FloatField(_(u"Quotation"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u"Company")
        verbose_name_plural = _(u"Companies")
