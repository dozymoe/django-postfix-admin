from django.conf import settings
from django.db import models
#-
from mail_domain.models import MailDomain

class MailUser(models.Model):

    email = models.CharField(max_length=100, unique=True, db_index=True)
    domain = models.ForeignKey(MailDomain, on_delete=models.PROTECT,
            db_index=True)
    password = models.CharField(max_length=255)
    password_cram_md5 = models.CharField(max_length=255)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False,
            db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'virtual_users'
        ordering = ['email']


    def __str__(self):
        return str(self.email)
