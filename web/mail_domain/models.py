from django.conf import settings
from django.db import models

class MailDomain(models.Model):

    name = models.CharField(max_length=50, unique=True, db_index=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False,
            db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'virtual_domains'
        ordering = ['name']


    def __str__(self):
        return str(self.name)
