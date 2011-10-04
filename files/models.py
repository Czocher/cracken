from django.utils.translation import ugettext_lazy as _
from django.db import models


class File(models.Model):
    path = models.CharField(_(u"Path"), max_length=255, unique=True)
    content = models.TextField(_(u"Content"))
    binary = models.BooleanField(_(u"Binary"), default=False)

    def name(self):
        return path.split('/')[-1]

    def __unicode__(self):
        return self.name(self)

    class Meta:
        verbose_name = _(u"File")
        verbose_name_plural = _(u"Files")
