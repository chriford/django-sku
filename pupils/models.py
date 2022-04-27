from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from authentication.models import User
from .subjects import Subjects

class Question(models.Model):
    STATUS_CHOICES = (
        ("pending", "pending"),
        ("completed", "completed"),
        ("rejected", "rejected"),
    )
    slug = models.SlugField(
        _("Slug"),
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
        _("Question"),
        max_length=300,
    )
    ban_count = models.IntegerField(
        null=True, 
        blank=True, 
        default=0,
    )
    status = models.CharField(
        _("status"),
        choices=STATUS_CHOICES,
        max_length=10
    )

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.subject}-" + slugify(self.subject | self.user)
        super(self, Question).save(*args, **kwargs)

