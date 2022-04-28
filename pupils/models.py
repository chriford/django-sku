from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from authentication.models import User

class Subjects(models.Model):
    subject = models.CharField(
        _("Subject"),
        max_length=30,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Question(models.Model):
    STATUS_CHOICES = (
        ("pending", "pending"),
        ("completed", "completed"),
        ("rejected", "rejected"),
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        editable=False,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    subject = models.ForeignKey(
        to=Subjects,
        on_delete=models.CASCADE,
    )
    question = models.TextField(
        verbose_name=_("Question"),
        max_length=300,
    )
    ban_count = models.IntegerField(
        verbose_name=_("Banned count"),
        null=True, 
        blank=True, 
        default=0,
    )
    status = models.CharField(
        verbose_name=_("status"),
        choices=STATUS_CHOICES,
        max_length=10
    )

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.subject}-" + slugify(self.subject | self.user)
        
        
        super(self, Question).save(*args, **kwargs)

