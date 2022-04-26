from django.db import models
from django.utils.translation import gettext_lazy as _

class Subjects(models.Model):
    subject = models.CharField(
        _("Subject"),
        max_length=30,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return self.subject