from django.conf import settings
from django.db import models
#-
from mail_domain.models import MailDomain

class MailAlias(models.Model):

    source = models.CharField(max_length=100, db_index=True)
    destination = models.CharField(max_length=100)
    domain = models.ForeignKey(MailDomain, on_delete=models.PROTECT,
            db_index=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False,
            db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'virtual_aliases'
        ordering = ['source']


    def __str__(self):
        return str(self.source)
